import csv,collections,time,pandas,unittest,os

class TestCases(unittest.TestCase):
    print("..... Now Running Unit TestCases .....")
    expected = 0
    actual = 0

    def test_checkForInput(self):
        print("Checking if both the files are present in the current folder")
        self.assertEqual(os.path.isfile('vlans.csv'),True)
        self.assertEqual(os.path.isfile('requests.csv'),True)

    def test_checkForAvailableColumn(self):
        print("Checking if required columns are present")
        with open('vlans.csv', 'r') as file:
            reader = csv.reader(file)
            row = next(reader)
            self.assertEqual(row[0],"device_id")
            self.assertEqual(row[1], "primary_port")
            self.assertEqual(row[2], "vlan_id")

    def test_checkIfData(self):
        print("Checking if valid data is available")
        with open('vlans.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)
            row = next(reader)
            self.assertEqual(row[0].isdigit(),True)
            self.assertEqual(row[1].isdigit(),True)
            self.assertEqual(row[2].isdigit(), True)

    def test_numberOfRows(self):
        print("check for expected rows vs. actual rows")
        self.assertEqual(self.expected,self.actual,"Equal")


if __name__ == '__main__':
    start = time.time()
    primary_port = []
    secondary_port = collections.defaultdict(set)
    op = []
    expected_rows = 0
    redundant_vlans = 0
    total=0
    with open('vlans.csv','r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row[1] == '1':
                primary_port.append((int(row[2]),int(row[0])))
            elif row[1] == '0':
                secondary_port[int(row[0])].add(int(row[2]))
        primary_port.sort()

    with open('requests.csv', 'r') as f:
        r = csv.reader(f)
        next(f)
        for ele in r:
            req_id = int(ele[0])
            redundancy  = int(ele[1])
            if redundancy == 0:
                data = primary_port.pop(0)
                op.append((req_id,data[1],1,data[0]))
                expected_rows+=1
            else:
                i = 0
                redundant_vlans += 1
                while True:
                    temp = primary_port[i]
                    if temp[0] in secondary_port[temp[1]]:
                        op.append((req_id, temp[1], 1, temp[0]))
                        op.append((req_id, temp[1], 0, temp[0]))
                        secondary_port[temp[1]].remove(temp[0])
                        primary_port.remove(temp)
                        break

                    i+=1
    op = sorted(op,key=lambda x:(x[0],x[2]))
    expected_rows+=(redundant_vlans*2)
    with open('output.csv', 'w',newline='') as op_1:
        csv_out = csv.writer(op_1)
        csv_out.writerow(['request_id', 'device_id','primary_port','vlan_id'])
        for row in op:
            csv_out.writerow(row)
            total+=1

    print("Time Required to run the code: - ",time.time()-start)
    TestCases.expected = expected_rows
    TestCases.actual = total
    unittest.main()
    print(expected_rows, total)

