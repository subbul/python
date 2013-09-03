#example to show various list operations

daysOfWeek = ["Tuesday","Wednesday"]
print "Initial List ", daysOfWeek

daysOfWeek.append('Thursday')

print "Appended list", daysOfWeek

daysOfWeek.insert(0,'Monday')

print "Inserted list ", daysOfWeek

daysOfWeek.extend(['Friday','saturday','sunday'])

print "Extended list", daysOfWeek

daysOfWeek.append('TempDay')

print "New list", daysOfWeek

print "Position of Wednesday in a week",daysOfWeek.index('Wednesday')

daysOfWeek.remove('TempDay')
print "Clean list", daysOfWeek

print "Poping  saturday",daysOfWeek.pop(5)

print daysOfWeek