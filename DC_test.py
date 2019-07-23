from ics import Calendar, Event
c = Calendar()
e = Event()
e.name = "K-WORLD FESTA"
e.begin = '2019-08-15 18:30:00'
e.end = '2019-08-15 23:59:59'
e.description = 'K-WORLD FESTA Opening Concert'
e.location = 'KSPO DOME'
e.url = 'https://www.kworldfesta.com/kspodome'
#e.categories = ''
#e.status = 'Group'
c.events.add(e)
c.events
# {<Event 'K-World Festa' begin:2019-08-15 18:00:00 end:2019-08-15 21:00:00>}
with open('DC.ics', 'w') as f:
	f.writelines(c)
# And it's done!
