from IPython.display import display

import pandas as pd
import numpy as np
import datetime
import plotly.express as px

from misc import percent

def infos(df, nb=5, random=False): 
    """Get shape and extract of a dataframe."""

    print('Shape: ', df.shape)
    if random: display(df.sample(nb))
    else: display(df.head(nb))


def na_analyze(df, verbose=True):
    """Print out an analyze of NAN in the dataframe."""

    row_number = df.shape[0]
    col_number = df.shape[1]
    nan_number = df.isna().sum().sum()
    nan_columns = df.isna().sum()
    nan_columns_filtered = {key:value for (key, value) in nan_columns.items()}
    nan_columns_filtered = [{'col_name': key, 'na_nb': value, 'na_percent': value / row_number} for (key, value) in nan_columns_filtered.items()]

    if verbose: print('Total NaN number:', nan_number, '(' + percent(nan_number / (row_number * col_number)) + ')')

    if nan_number == 0: return

    nan_columns_filtered.sort(key=lambda x: x['na_nb'], reverse=True)

    for obj in nan_columns_filtered:
        if obj['na_nb'] == 0: continue

        if verbose:
            prcnt = percent(obj['na_percent'])
            col_name = str(obj['col_name'])
            print(f' - {prcnt} of column <{col_name}> is not defined')


def column_analyze(df, column_name, nb=20):
    """Print out an analyse of values of a column."""

    uniques = df[column_name].unique()
    sumup = []

    for u in uniques:
        if pd.notna(u):
            sumup.append({
                "key": u,
                "count": (df[column_name] == u).sum()
            })
        else: 
            sumup.append({
                "key": "None",
                "count": (df[column_name].isna()).sum()
            })
    sumup.sort(key=lambda elt: elt['count'], reverse=True)

    print(f'{len(sumup)} unique values:')
    for i in range(min(nb, len(sumup))):
        print(percent(sumup[i]["count"] / len(df)) + f': "{sumup[i]["key"]}" ==> {sumup[i]["count"]}')
    

def histogram(df, column_name, title='', max_number=20, width=None, height=None, style='bar', colors=None):
    """Print out an horizontal histogram of a DataFrame column."""

    temp_df = df.copy()
    temp_df[column_name] = temp_df[column_name].astype(str)
    counts = temp_df.groupby(column_name).count()
    counts = counts.reset_index()[[column_name, counts.columns[0]]].sort_values(counts.columns[0], ascending=True)
    counts.rename(columns={counts.columns[1]:'Count'}, inplace=True)
    total_nb = counts['Count'].sum()
    counts['Percent'] = round((counts['Count'] / total_nb) * 1000) / 10
    counts['Percent'] = counts['Percent'].astype(str) + ' %'

    if style == 'bar':
        fig = px.bar(counts[-max_number:], x="Count", y=column_name, orientation='h', text="Percent", title=title, width=width, height=height)
    else:
        fig = px.pie(counts, values='Count', names=column_name, title=title, color_discrete_sequence=colors)
        fig.update_traces(textposition='inside', textinfo='percent+label', showlegend=False)

    fig.show()


def discover(df, uniq_ex_nb=5):
    """Get an rough analysis of the dataframe."""

    print('Columns contain:')

    # Get the size of the longer column name
    col_name_size = 0
    for col in df.columns:
        if len(col) > col_name_size: col_name_size = len(col)

    # Unique values str size
    uniq_val_size = len(str(len(df)))

    # How much row is there?
    print(f'Total number of rows: {df.shape[0]}')


    def display_ex(value):
        if len(str(value)) > 10: return str(value)[0:10] + '...'
        return str(value)

    # Discover each column (na number, unique values)
    nas = df.isna().sum().sort_values()
    for key, val in nas.iteritems():
        to_print = '  - ' + f'"{key}"'.rjust(col_name_size + 2) + ': '
        to_print += f'{percent(val / df.shape[0])} empty - '
        extract = '; '.join([display_ex(v) for v in df[key].unique()[:uniq_ex_nb]])
        uniq_nb = len(df[key].unique())
        uniq_prct = uniq_nb / df.shape[0]
        to_print += f'{uniq_nb}'.rjust(uniq_val_size)
        to_print += f' ({percent(uniq_prct)}) uniques (eg: {extract})'
        print(to_print)


def set_types(df, types):
    for key in types:
        try:
            if types[key] == 'int': df[key] = df[key].astype(pd.Int64Dtype())
            if types[key] == 'float': df[key] = df[key].astype(pd.Float64Dtype())
            if types[key] == 'string': df[key] = df[key].astype(pd.StringDtype())
            if types[key] == 'boolean': df[key] = df[key].astype(bool)
            if 'datetime:' in types[key] : 
                df[key] = df[key].astype(pd.StringDtype())
                format = types[key].replace('datetime:', '')
                df[key] = [datetime.datetime.strptime(dt, format) if pd.notna(dt) else pd.NaT for dt in df[key]]
        except ValueError:
            raise ValueError(f'Error trying to parse column <{key}> into <{types[key]}>')