from datetime import datetime

hw_path = 'hw.csv'
tests_path = 'tests.csv'

def sortFunc(row):
    date_string = row.split('\t')[3]
    date_object = datetime.strptime(date_string, '%a %m/%d/%y')

    return (date_object - datetime(1970,1,1)).days



def get_hw():
    f = open(hw_path, 'r')
    hw = f.read()
    f.close()

    hw_template = '''
        <tr>
            <td>// class //</td>
            <td>// assignment //</td>
            <td>// due //</td>
            <td>// submit //</td>
            <td>
                <form method="GET" action="edit_hw.py">
                    <input type="hidden" name="id" value="// id //">
                    <button class="button is-small is-info is-light" type="submit"><i class="fas fa-pencil-alt"></i></button>
                </form>
            </td>
            <td>
                <form method="GET" action="complete_hw.py">
                    <input type="hidden" name="id" value="// id //">
                    <button class="button is-small is-success is-light" type="submit"><i class="fas fa-check"></i></button>
                </form>
            </td>
        </tr>
    '''

    entries = ''
    hw_rows = []

    for row in hw.split('\n')[0:-1]:
        elements = row.split('\t')
        completed = elements[6]
        if completed == 'True':
            continue

        hw_rows.append(row)

    hw_rows.sort(key=sortFunc)

    for row in hw_rows:
        elements = row.split('\t')
        subject = elements[1]
        assignment = elements[2]
        due = elements[3]
        submit = elements[4]
        link = elements[5]
        id = elements[0]

        if link != '':
            submit = '<a href="' + link + '" target="_blank">' + submit + '</a>'
        
        entry = hw_template.replace('// class //', subject)
        entry = entry.replace('// assignment //', assignment)
        entry = entry.replace('// due //', due)
        entry = entry.replace('// submit //', submit)
        entry = entry.replace('// id //', id)
        
        entries += entry

    return entries

def get_tests():
    f = open(tests_path, 'r')
    tests = f.read()
    f.close()

    tests_template = '''
        <tr>
            <td>// class //</td>
            <td>// test //</td>
            <td>// date //</td>
            <td>
                <form method="GET" action="edit_test.py">
                    <input type="hidden" name="id" value="// id //">
                    <button class="button is-small is-info is-light" type="submit"><i class="fas fa-pencil-alt"></i></button>
                </form>
            </td>
            <td>
                <form method="GET" action="complete_test.py">
                    <input type="hidden" name="id" value="// id //">
                    <button class="button is-small is-success is-light" type="submit"><i class="fas fa-check"></i></button>
                </form>
            </td>
        </tr>
    '''

    entries = ''
    tests_rows = []

    for row in tests.split('\n')[0:-1]:
        elements = row.split('\t')
        completed = elements[4]
        if completed == 'True':
            continue

        tests_rows.append(row)

    tests_rows.sort(key=sortFunc)

    for row in tests_rows:
        elements = row.split('\t')
        subject = elements[1]
        test = elements[2]
        date = elements[3]
        id = elements[0]
        
        entry = tests_template.replace('// class //', subject)
        entry = entry.replace('// test //', test)
        entry = entry.replace('// date //', date)
        entry = entry.replace('// id //', id)
        
        entries += entry

    return entries
