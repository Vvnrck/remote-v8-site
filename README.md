# remote-v8-site

This is a part of my experimental project I wrote ~1 year ago.
The idea was to implement a client-server system for distributed computing based on simple application-level technologies.

- The client is a C++/Qt app with built-in JavaScript V8 engine for the actual computing. 
- The server is a Django app where customers leave their JS and CSV data. It also provides HTTP API for the client app and responsible for benchmarking.

Customers have "points" that are similar to money. The points are transfered to clients based on how long it took them to complete the task. Random 10% of tasks are actually hidden benchmarks to prevent fraud and to adjust client's "hourly rate".
