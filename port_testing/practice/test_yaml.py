import yaml


def test_yaml():
    env = {
        "default":"dev",
        "testing":
        {
        "dev" : "127.0.0.1",
        "test" : "127.0.0.2"
         }
    }

    #把env的json格式转换位yaml文件
    with open("env.yaml","w") as f:
        yaml.safe_dump(data=env,stream=f)