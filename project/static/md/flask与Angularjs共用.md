title: flask与Angularjs共用
date: 2014-09-02 19:55:34
---
解决办法 1：
替换 AngularJS 中使用的标识符
```cmd
app = angular.module('TheApp', [], ($interpolateProvider) ->
  $interpolateProvider.startSymbol('{$')
  $interpolateProvider.endSymbol('$}')
)
```cmd
解决办法 2（推荐）：
替换 Jinja2 中使用的标识符（在 Flask 下）
```
app.jinja_env.variable_start_string = '${'
app.jinja_env.variable_end_string = '}'
```