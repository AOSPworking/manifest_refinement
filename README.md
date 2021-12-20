# manifest_refinement

## 1. Usage

只要把那个 2.7 个 `GB` 的 `build.ninja` 放到这个目录下，就可以开始精简它：

```shell
> python refine.py
```

会输出一个叫做 `new-build.ninja` 的文件。这个文件里面包括所有 `frameworks` 中定义的模块。

## 2. Test

在输出 `new-build.ninja` 之后，可以通过：

```shell
> python test.py
```

测试下获取的到底完不完全。我测出来是没错的，`build.ninja` 和 `new-build.ninja` 都是 6483 个模块。
