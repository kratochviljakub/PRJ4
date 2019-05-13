def transfer_SVO_traj(input_name, output_name):
    input_file = open(input_name, 'r')
    output_file = open(output_name, 'w')

    input_lines = input_file.readlines()
    counter_lines = 1
    for line in input_lines:
        if counter_lines == 4:
            s = line.replace('    secs: ', '')
            s = s.replace('\n', '')
            output_file.write(s)
            output_file.write('.')
        if counter_lines == 5:
            s = line.replace('  nsecs: ', '')
            s = s.replace('\n', '')
            s = str(int(s))
            output_file.write(s)
            output_file.write(' ')
        if counter_lines == 10:
            s = line.replace('    x: ', '')
            s = s.replace('\n', '')
            s = s.replace(' ','')
            output_file.write(s)
            output_file.write(' ')
        if counter_lines == 11:
            s = line.replace('    y: ', '')
            s = s.replace('\n', '')
            s = s.replace(' ', '')
            output_file.write(s)
            output_file.write(' ')
        if counter_lines == 12:
            s = line.replace('    z: ', '')
            s = s.replace('\n', '')
            s = s.replace(' ', '')
            output_file.write(s)
            output_file.write(' ')
        if counter_lines == 14:
            s = line.replace('    x: ', '')
            s = s.replace('\n', '')
            s = s.replace(' ', '')
            output_file.write(s)
            output_file.write(' ')
        if counter_lines == 15:
            s = line.replace('    y: ', '')
            s = s.replace('\n', '')
            s = s.replace(' ', '')
            output_file.write(s)
            output_file.write(' ')
        if counter_lines == 16:
            s = line.replace('    z: ', '')
            s = s.replace('\n', '')
            s = s.replace(' ', '')
            output_file.write(s)
            output_file.write(' ')
        if counter_lines == 17:
            s = line.replace('    w: ', '')
            s = s.replace('\n', '')
            s = s.replace(' ', '')
            output_file.write(s)
            output_file.write('\n')

        counter_lines += 1
        if counter_lines > 19:
            counter_lines = 1


def transfer_SVO_gt(input_name, output_name):
    input_file = open(input_name, 'r')
    output_file = open(output_name, 'w')

    input_lines = input_file.readlines()
    counter_lines = 1
    for line in input_lines:
        if counter_lines == 4:
            s = line.replace('    secs: ', '')
            s = s.replace('\n', '')
            output_file.write(s)
            output_file.write('.')
        if counter_lines == 5:
            s = line.replace('  nsecs: ', '')
            s = s.replace('\n', '')
            s = str(int(s))
            output_file.write(s)
            output_file.write(' ')
        if counter_lines == 9:
            s = line.replace('    x: ', '')
            s = s.replace('\n', '')
            output_file.write(s)
            output_file.write(' ')
        if counter_lines == 10:
            s = line.replace('    y: ', '')
            s = s.replace('\n', '')
            output_file.write(s)
            output_file.write(' ')
        if counter_lines == 11:
            s = line.replace('    z: ', '')
            s = s.replace('\n', '')
            output_file.write(s)
            output_file.write(' ')
        if counter_lines == 13:
            s = line.replace('    x: ', '')
            s = s.replace('\n', '')
            output_file.write(s)
            output_file.write(' ')
        if counter_lines == 14:
            s = line.replace('    y: ', '')
            s = s.replace('\n', '')
            output_file.write(s)
            output_file.write(' ')
        if counter_lines == 15:
            s = line.replace('    z: ', '')
            s = s.replace('\n', '')
            output_file.write(s)
            output_file.write(' ')
        if counter_lines == 16:
            s = line.replace('    w: ', '')
            s = s.replace('\n', '')
            output_file.write(s)
            output_file.write('\n')

        counter_lines += 1
        if counter_lines > 17:
            counter_lines = 1

def transfer_traj_LSD(input_name, output_name, gt_name):
    input_file = open(input_name, 'r')
    output_file = open(output_name, 'w')
    gt_file = open(gt_name, 'r')

    gt_line = gt_file.readline()
    s = gt_line.split(' ')
    s = s[0].split('.')
    secs = int(s[0])
    nsecs = int(s[1])

    input_lines = input_file.readlines()
    counter_lines = 1
    for line in input_lines:
        if counter_lines == 4:
            s = line.replace('    secs: ', '')
            tmp = str(int(s) + secs)
            output_file.write(tmp)
            output_file.write('.')
        if counter_lines == 5:
            s = line.replace('   nsecs: ', '')
            tmp = str(int(s) + nsecs)
            output_file.write(tmp)
            output_file.write(' ')
        if counter_lines == 9:
            s = line.replace('    x: ', '')
            s = s.replace('\n', '')
            output_file.write(s)
            output_file.write(' ')
        if counter_lines == 10:
            s = line.replace('    y: ', '')
            s = s.replace('\n', '')
            output_file.write(s)
            output_file.write(' ')
        if counter_lines == 11:
            s = line.replace('    z: ', '')
            s = s.replace('\n', '')
            output_file.write(s)
            output_file.write(' ')
        if counter_lines == 13:
            s = line.replace('    x: ', '')
            s = s.replace('\n', '')
            output_file.write(s)
            output_file.write(' ')
        if counter_lines == 14:
            s = line.replace('    y: ', '')
            s = s.replace('\n', '')
            output_file.write(s)
            output_file.write(' ')
        if counter_lines == 15:
            s = line.replace('    z: ', '')
            s = s.replace('\n', '')
            output_file.write(s)
            output_file.write(' ')
        if counter_lines == 16:
            s = line.replace('    w: ', '')
            s = s.replace('\n', '')
            output_file.write(s)
            output_file.write('\n')

        counter_lines += 1
        if counter_lines > 17:
            counter_lines = 1


def main():
    transfer_traj_LSD('LSD_trajectory_11.txt', 'result_lsd_11.txt', 'groundtruthSync_11.txt')
    transfer_SVO_gt('SVO_ground_truth.txt', 'groundtruth_SVO.txt')
    transfer_SVO_traj('SVO_trajektorie.txt', 'result_svo.txt')


if __name__ == '__main__':
    main()
