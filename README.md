
### To Install
1. create a python 3.10 venv `python -m venv` and activate `source venv/bin/activate`
2. install dependencies `pip install -r requirements.txt`

### To Test
1. run with `python -m pytest tests`

### To Run (live)
1. export ENV="live"
2. update the values in the `.env` file to the live values
3. run with `python main.py`

### To Run (mock)
_(requires docker)_
1. export ENV="mock"
2. start the mock api server with `docker-compose up`
3. run with `python main.py`

### What was the plan?

I created a little command-line utility that allows you to specify the `site_id`
for the outages you want to upload. I split each step out into separate functions
to make them easier to test. Some of the tests are a bit pointless - like testing
to see if the mocked API returns what I've told it to - though this did help when
setting up the test suite because mocking things is always interesting. The unit
tests were all built from the example in the instructions.

I tried to generate a mock API I could test against locally (and in theory in CI etc)
but my usual go to - Postman mock server - was just not playing ball today. For some
reason it was having a real problem with the API key auth. I spent long enough messing
about with it and eventually decided to spin up a Prism server which... mostly.. works.
That has problems with the POST, my payload looks to me to be in the correct format (and
it submits with no errors to the live API) but whatever I do I get a 422. I have not
looked into whether this is Prism or the openapi specs, I figured I'd make the most
of it and use it to test an HTTP error code as the format is covered by a unit test.

Exception handling is not pretty. I could definitely use something better than just plain
`Exception` for everything but I didn't see the need for it in such a small app. The stuff
at the start with the `requests.Retry` *should* manage the case when we get a surprise 500
by retrying 5 times with an exponential(?) backoff so as not to hammer your servers when they
are already struggling! I can't test this locally though because of the local API server
issues I had.

I used env vars to keep the live and mock details separate. I did start with instructions
for you to put in your own API key so I didn't have to commit mine but then I re-read your
readme so added the live ones in there too. You can swap between the two easily though, I
like to always try and run things locally first as much as I can.

This seems too simple, like I've missed something and not done enough...