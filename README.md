# Byteplus Python SDK

## Installation
require python version >= 2.7

```
    pip install --user byteplus-sdk
```

Upgrade sdk version from old one
```
    pip install --upgrade byteplus-sdk
```

## About AK/SK

### AK/SK registration procedure
Main account and privileged sub-account may create AK/SK pair:

Log in to byteplus console
Choose "IAM" -> "Key Management"
You can find AK/SK pair details in the page, each account can have maximum of 2 pairs.
Create new token or click to view key detail.

### AK/SK usage in sdk

- (option 1 recommand) Use set_ak/set_sk in code：
  ```python
      iam_service = IamService()
      # call below method if you dont set ak and sk in $HOME/.byteplus/config
      iam_service.set_ak('ak')
      iam_service.set_sk('sk')
  ```

- (option 2) Set in env variable 
  ```bash
  BYTEPLUS_ACCESSKEY="your ak"  
  BYTEPLUS_SECRETKEY="your sk"
  ```
- (option 3) json file at ～/.byteplus/config：
  ```json
    {"ak":"your ak","sk":"your sk"}
  ```

## Region Setting

- Currently one region is active

  ```
  - ap-singapore-1
  ```

- Default ap-singapore-1, Specify region as param in init function if needed：
  
  ```
  iam_service = IamService('us-east-1')
  ```
