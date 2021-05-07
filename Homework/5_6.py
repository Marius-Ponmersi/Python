with open('5_6.txt', 'r', encoding='UTF-8') as f_read:
    spisok_strok = f_read.readlines()
    subjects_list = []
    hours_list = []
    print(spisok_strok)

    for stroka in spisok_strok:

        lecture = stroka.split()[1]
        practice = stroka.split()[2]
        lab = stroka.split()[3]

        if lecture == '-':
            lecture = 0
        else:
            lecture = int(lecture[:lecture.find('(')])
        if practice == '-':
            practice = 0
        else:
            practice = int(practice[:practice.find('(')])
        if lab == '-':
            lab = 0
        else:
            lab = int(lab[:lab.find('(')])

        hours = lecture + practice + lab
        subjects_list.append(stroka.split()[0])
        hours_list.append(hours)

    subjects = dict(zip(subjects_list, hours_list))
    print(subjects)
