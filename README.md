# autoapitest
auto api test by python3, 
Simulate browser requests

## build docker image

```
docker build -t autoapitest:latest .
```

## creat test case
create your yaml file like:
```
spec:
- name: Test chrome mac
  host: http://test.domain
  headers:
    accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8
    referer: https://test.domain/
    user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36
  cases:
  - name: test api one
    request:
      url: /api/v1/testapple
    want:
      status: 200
      length: 6263
      type: content/json
      md5: abcdefg1234567
  - name: test api two
    request:
      url: /app/v2/testbanana
    want:
      status: 200
      length: 3564
      type: content/json
```

## run test

if run by shell

```
# pip3 install -r requirements.txt
python3 run.py
```

if run by docker
```
docker run -it --rm -v $(pwd):/test autoapitest:latest
```