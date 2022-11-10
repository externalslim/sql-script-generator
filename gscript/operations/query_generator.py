import pandas as pnd

class QueryGenerator:

    @staticmethod
    
    def script_generate(data_frame):

        ### definitions ###
        counter = 0
        script = ''
        script_array = []

        row_length = len(data_frame.index)
 
        for _ in range(round((row_length / 1000) + 0.1)):
            row_array = []
            for i in range(1, counter):
                row_array.append(i)
            counter += 1000
            if len(row_array) > 0:
                another_data_frame = pnd.read_excel('data_gscript.xlsx', header=0, nrows=1000, skiprows=row_array)
                script = QueryGenerator.script_builder('tablo', another_data_frame)
                script_array.append(script)
            else:
                another_data_frame = pnd.read_excel('data_gscript.xlsx', header=0, nrows=999, skiprows=[])
                script = QueryGenerator.script_builder('tablo', another_data_frame)
                script_array.append(script)
            row_array = []

        return script_array

    @staticmethod
    def script_builder(table, data_frame):

        columns = QueryGenerator.insert_columns(data_frame)
        values = QueryGenerator.insert_values(data_frame)

        return 'insert into ' + table + columns + values

    @staticmethod
    def insert_columns(data_frame):
        data_frame_items = data_frame.items()
        insert_columns = '('

        for key, value in data_frame_items:
            str_key = str(key)
            if ':' in str_key:
                insert_columns += str(str_key.split(':', 1)[0]) + ','
            else:
                insert_columns += str_key + ','
        insert_columns = insert_columns[:-1] + ') values \n'
        return insert_columns

    @staticmethod
    def insert_values(data_frame):
        values = ''

        for rows in data_frame.to_dict(orient='records'):
            row_val = '('
            for key, value in rows.items():
                str_value = str(value)
                if ':' in key:
                    row_val += str(str_value.split(':', 1)[0]) + ','
                else:
                    row_val += '\'' + str_value + '\','
            row_val = row_val[:-1] + '), \n'
            values += row_val
        values = values[:-3]
        return values