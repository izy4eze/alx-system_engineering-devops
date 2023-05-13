ST POSTMORTEM

Cause of  the slow web server

We encountered a slow web server on March 23, 2023, which prevented our clients from using our services, and we sincerely apologize for any financial loss our clients experienced during this time.

Issue Summary
This was a result of unprecedented traffic on our web server, where there was excessive overhead on our web server, which was over the capacity it was initially built for. As an effect of this, the server keeps halting there, not allowing our client to successfully transact on the website, This resulted in a 100% impact on their business as they were unable to access our services. 


Timeline (all time in GMT + 1)







Time (GMT + 1)
Actions
12: 00 PM
Upgrades implementation begins
12:10 PM
Server slag begins
12:11 PM
Pagers alerted the on-call team
12:20 PM
On-call team acknowledgment
12:25 PM
Rollback initiation begins
12:35 PM
Successful rollback
12:40 PM
Server restart initiated
12: 45 PM
100% of traffic back online













Root cause



Overhead refers to unnecessary items in your site's database, such as logs, transients, and other entries from plugins or themes. Excessive "overhead" might cause database searches to take longer than necessary. In some situations, it can even cause your web server to time out while waiting for a response from your database.

Preventive measures
There was no redundancy before the incident so we implemented a redundant server and load balance to distribute traffic evenly among the servers




