# Be More Pythonic

从GitHub的提交记录可以注意到，我提交的绝大部分代码都是Python编写的，我也确实对着门语言最中意。

本文将记录一些经常被遗忘的技巧和语法糖。内容来源于[Python 工匠](https://github.com/piglei/one-python-craftsman/blob/master/zh_CN/1-using-variables-well.md)和[Python 进阶](https://py.eastlakeside.cn/)。

## 变量使用

- 避免`globals`和`locals`。这些函数将返回包含全局/局部的字典。
  
- 合理使用 namdtuple 和 dict 作为函数返回值。比如：
  

```python
def latlon_to_address(lat, lon):
    return {
        'country': country,
        'province': province,
        'city': city
    }
# 
Address = namedtuple("Address", ['country', 'province', 'city'])

def latlon_to_address(lat, lon):
    return Address(
        country=country,
        province=province,
        city=city
    )
```

## 分支代码

- 避免嵌套，合并分支，封装逻辑；
  
- 为对象定义`__bool__`方法，该方法将会作为`bool(obj())`的返回值。
  
  - 如果没有`__bool__`方法，将会调用`__len__`方法，可应用于节省长度判断。
    
- `all()`和`any()`函数：对参数中的所有对象进行布尔判断。如：
  

```python
def all_numbers_gt_10_2(numbers):
    return bool(numbers) and all(n > 10 for n in numbers)
```

- 在 try/while/for 中使用 else 分支；
  
  - 若没有抛出异常，则执行 else 分支。
    

```python
def do_stuff():
    try:
        do_the_first_thing()
    except Exception as e:
        print("Error while calling do_some_thing")
        return
    else:
        return do_the_second_thing()
```

- == 和 is 的区别
  
  - == 仅判断两者所指向的值是否相同，而 is 会判断是否指向内存中的同一内容
    
  - 判断是否为 None 时应使用 is ！！！
    
  - 因为`__eq__`方法可以绕过 == 比较
    
- and 的优先级大于 or，所以 x and a or b 不是总能给出正确的结果
  
  - 有趣的例子：`True and None or 0`
    

####
