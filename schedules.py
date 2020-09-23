def get_schedule(letter, periods):
    if periods == '1-5':
        return '''
            <tr>
                <th>1</th>
                <td>9:10 AM - 10:05 AM</td>
                <td>AP US History</td>
            </tr>
            <tr>
                <th>2</th>
                <td>10:15 AM - 11:10 AM</td>
                <td>Calc BC</td>
            </tr>
            <tr>
                <th>3</th>
                <td>11:20 AM - 12:15 PM</td>
                <td>Calc BC</td>
            </tr>
            <tr>
                <th>4</th>
                <td>12:25 PM - 1:20 PM</td>
                <td>Free Period</td>
            </tr>
            <tr>
                <th>5</th>
                <td>1:30 PM - 2:25 PM</td>
                <td>AP Spanish</td>
            </tr>
        '''
    elif letter == 'A' and periods == '6-10':
        return '''
            <tr>
                <th>6</th>
                <td>9:10 AM - 10:05 AM</td>
                <td>Physics Lab</td>
            </tr>
            <tr>
                <th>7</th>
                <td>10:15 AM - 11:10 AM</td>
                <td>Physics</td>
            </tr>
            <tr>
                <th>8</th>
                <td>11:20 AM - 12:15 PM</td>
                <td>AP English</td>
            </tr>
            <tr>
                <th>9</th>
                <td>12:25 PM - 1:20 PM</td>
                <td>Health Ed</td>
            </tr>
            <tr>
                <th>10</th>
                <td>1:30 PM - 2:25 PM</td>
                <td>AP Comp Sci</td>
            </tr>
        '''
    elif letter == 'B' and periods == '6-10':
        return '''
            <tr>
                <th>6</th>
                <td>9:10 AM - 10:05 AM</td>
                <td>Phys Ed</td>
            </tr>
            <tr>
                <th>7</th>
                <td>10:15 AM - 11:10 AM</td>
                <td>Physics</td>
            </tr>
            <tr>
                <th>8</th>
                <td>11:20 AM - 12:15 PM</td>
                <td>AP English</td>
            </tr>
            <tr>
                <th>9</th>
                <td>12:25 PM - 1:20 PM</td>
                <td>Health Ed</td>
            </tr>
            <tr>
                <th>10</th>
                <td>1:30 PM - 2:25 PM</td>
                <td>AP Comp Sci</td>
            </tr>
        '''
    else:
        return ''
