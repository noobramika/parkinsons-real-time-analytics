SELECT * from test1;

--Create a stream to track changes on the table
CREATE STREAM test1_stream ON TABLE test1;

-- monitor the stream
SELECT * FROM test1_stream;