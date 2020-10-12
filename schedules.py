def get_schedule(letter, periods):
    if periods == '1-5':
        return '''
            <tr>
                <th>1</th>
                <td>9:10 AM - 10:05 AM</td>
                <td><a href="https://classroom.google.com/u/0/c/MTU5ODcyMTk0NTQ3" target="_blank">AP US History</a></td>
            </tr>
            <tr>
                <th>2</th>
                <td>10:15 AM - 11:10 AM</td>
                <td><a href="https://us02web.zoom.us/j/83208699689?pwd=SDJrUnBZK3JOU0dxSjREUnN0WkQ0QT09" target="_blank">Calc BC</a></td>
            </tr>
            <tr>
                <th>3</th>
                <td>11:20 AM - 12:15 PM</td>
                <td><a href="https://us02web.zoom.us/j/83208699689?pwd=SDJrUnBZK3JOU0dxSjREUnN0WkQ0QT09" target="_blank">Calc BC</a></td>
            </tr>
            <tr>
                <th>4</th>
                <td>12:25 PM - 1:20 PM</td>
                <td>Free Period</td>
            </tr>
            <tr>
                <th>5</th>
                <td>1:30 PM - 2:25 PM</td>
                <td><a href="https://us02web.zoom.us/j/86833907107?pwd=aC9SSnQvOGljVDRjQ052UzZ5TGlWZz09" target="_blank">AP Spanish</a></td>
            </tr>
        '''
    elif letter == 'A' and periods == '6-10':
        return '''
            <tr>
                <th>6</th>
                <td>9:10 AM - 10:05 AM</td>
                <td><a href="https://us02web.zoom.us/j/81053388988?pwd=aGFrRnNuTS9lREVqMmtOekxOT2lTZz09" target="_blank">Physics Lab/Free</a></td>
            </tr>
            <tr>
                <th>7</th>
                <td>10:15 AM - 11:10 AM</td>
                <td><a href="https://us02web.zoom.us/j/81053388988?pwd=aGFrRnNuTS9lREVqMmtOekxOT2lTZz09" target="_blank">Physics</a></td>
            </tr>
            <tr>
                <th>8</th>
                <td>11:20 AM - 12:15 PM</td>
                <td><a href="https://us02web.zoom.us/j/89706035693?pwd=NkRrOXNJSytjR1hGelAyMGVpTWhsQT09" target="_blank">AP English</a></td>
            </tr>
            <tr>
                <th>9</th>
                <td>12:25 PM - 1:20 PM</td>
                <td><a href="https://us02web.zoom.us/j/86086092283?pwd=dnpacVBlTmltTzYrWkRMdFNtM0paUT09" target="_blank">Health Ed</a></td>
            </tr>
            <tr>
                <th>10</th>
                <td>1:30 PM - 2:25 PM</td>
                <td><a href="https://us02web.zoom.us/j/84387765604?pwd=L2NRR2dITjdmTFpQRC9DTk10WnREZz09" target="_blank">AP Comp Sci</a></td>
            </tr>
        '''
    elif letter == 'B' and periods == '6-10':
        return '''
            <tr>
                <th>6</th>
                <td>9:10 AM - 10:05 AM</td>
                <td><a href="https://meet.google.com/lookup/djrrqrpag6?authuser=0&hs=179" target="_blank">Phys Ed</a></td>
            </tr>
            <tr>
                <th>7</th>
                <td>10:15 AM - 11:10 AM</td>
                <td><a href="https://us02web.zoom.us/j/81053388988?pwd=aGFrRnNuTS9lREVqMmtOekxOT2lTZz09" target="_blank">Physics</a></td>
            </tr>
            <tr>
                <th>8</th>
                <td>11:20 AM - 12:15 PM</td>
                <td><a href="https://us02web.zoom.us/j/89706035693?pwd=NkRrOXNJSytjR1hGelAyMGVpTWhsQT09" target="_blank">AP English</a></td>
            </tr>
            <tr>
                <th>9</th>
                <td>12:25 PM - 1:20 PM</td>
                <td><a href="https://us02web.zoom.us/j/86086092283?pwd=dnpacVBlTmltTzYrWkRMdFNtM0paUT09" target="_blank">Health Ed</a></td>
            </tr>
            <tr>
                <th>10</th>
                <td>1:30 PM - 2:25 PM</td>
                <td><a href="https://us02web.zoom.us/j/84387765604?pwd=L2NRR2dITjdmTFpQRC9DTk10WnREZz09" target="_blank">AP Comp Sci</a></td>
            </tr>
        '''
    else:
        return ''
