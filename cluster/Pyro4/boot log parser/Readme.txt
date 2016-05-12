Sebelum memulai worker, worker1, dan workersort jalankan
"python -m Pyro4.naming -n danang"
pada cmd

dispatcher bertugas untuk mengirim file log ke worker dan worker1
setelah itu dispatcher meminta hasil parsing dari worker dan worker1
setelah itu dispatcher mengirim hasil parsing dari worker dan worker1 ke workersort untuk di sort
setelah itu dispatcher mem-print hasil sort dari workersort