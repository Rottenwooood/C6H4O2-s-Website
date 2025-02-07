author: Ir1d, aofall, Marcythm

来自 [C++ 运算符优先级 - cppreference](https://zh.cppreference.com/w/cpp/language/operator_precedence) ，有修改。

|          运算符         |    描述    |                              例子                              | 可重载性 |
| :------------------: | :------: | :----------------------------------------------------------: | :--: |
|       **第一级别**       |          |                                                              |      |
|         `::`         |  作用域解析符  |                       `Class::age = 2;`                      | 不可重载 |
|       **第二级别**       |          |                                                              |      |
|         `++`         |  后自增运算符  |           `for (int i = 0; i < 10; i++) cout << i;`          |  可重载 |
|         `--`         |  后自减运算符  |           `for (int i = 10; i > 0; i--) cout << i;`          |  可重载 |
|   `type()  type{}`   |  强制类型转换  |           `unsigned int a = unsigned(3.14);`                | 可重载 |
|         `()`         |   函数调用   |                        `isdigit('1')`                        |  可重载 |
|         `[]`         |  数组数据获取  |                        `array[4] = 2;`                       |  可重载 |
|          `.`         |  对象型成员调用 |                        `obj.age = 34;`                       | 不可重载 |
|         `->`         |  指针型成员调用 |                       `ptr->age = 34;`                       |  可重载 |
|   **第三级别** （从右向左结合）  |          |                                                              |      |
|         `++`         |  前自增运算符  |             `for (i = 0; i < 10; ++i) cout << i;`            |  可重载 |
|         `--`         |  前自减运算符  |             `for (i = 10; i > 0; --i) cout << i;`            |  可重载 |
|          `+`         |    正号    |                         `int i = +1;`                        |  可重载 |
|          `-`         |    负号    |                         `int i = -1;`                        |  可重载 |
|          `!`         |   逻辑取反   |                        `if (!done) …`                       |  可重载 |
|          `~`         |   按位取反   |                       `flags = ~flags;`                      |  可重载 |
|       `(type)`       |  C 风格强制类型转换  |                 `int i = (int) floatNum;`             |  可重载 |
|          `*`         |   指针取值   |                     `int data = *intPtr;`                    |  可重载 |
|          `&`         |   值取指针   |                    `int *intPtr = &data;`                    |  可重载 |
|       `sizeof`       |  返回类型内存  |    `int size = sizeof floatNum; int size = sizeof(float);`   | 不可重载 |
|         `new`        | 动态元素内存分配 |  `long *pVar = new long; MyClass *ptr = new MyClass(args);`  |  可重载 |
|       `new []`       | 动态数组内存分配 |                 `long *array = new long[n];`                 |  可重载 |
|       `delete`       | 动态析构元素内存 |                        `delete pVar;`                        |  可重载 |
|      `delete []`     | 动态析构数组内存 |                      `delete [] array;`                      |  可重载 |
|       **第四级别**    |          |                                                              |      |
|         `.*`         |  类对象成员引用 |                       `obj.*var = 24;`                       | 不可重载 |
|         `->*`        |  类指针成员引用 |                       `ptr->*var = 24;`                      |  可重载 |
|       **第五级别**    |          |                                                              |      |
|          `*`         |    乘法    |                       `int i = 2 * 4;`                       |  可重载 |
|          `/`         |    除法    |                    `float f = 10.0 / 3.0;`                   |  可重载 |
|          `%`         | 取余数（模运算） |                      `int rem = 4 % 3;`                      |  可重载 |
|       **第六级别**    |          |                                                              |      |
|          `+`         |    加法    |                       `int i = 2 + 3;`                       |  可重载 |
|          `-`         |    减法    |                       `int i = 5 - 1;`                       |  可重载 |
|       **第七级别**    |          |                                                              |      |
|         `<<`         |    位左移   |                    `int flags = 33 << 1;`                    |  可重载 |
|         `>>`         |    位右移   |                    `int flags = 33 >> 1;`                    |  可重载 |
|       **第八级别**     |          |                                                              |      |
|         `<=>`         | 三路比较运算符  |                `if ((i <=> 42) < 0) ...`                      |  可重载 |
|       **第九级别**     |          |                                                              |      |
|          `<`         |    小于    |                      `if (i < 42) ...`                      |  可重载 |
|         `<=`         |   小于等于   |                      `if (i <= 42) ...`                     |  可重载 |
|          `>`         |    大于    |                      `if (i > 42) ...`                      |  可重载 |
|         `>=`         |   大于等于   |                      `if (i >= 42) ...`                     |  可重载 |
|       **第十级别**       |          |                                                              |      |
|         `==`         |    等于    |                      `if (i == 42) ...`                     |  可重载 |
|         `!=`         |    不等于   |                      `if (i != 42) ...`                     |  可重载 |
|       **第十一级别**      |          |                                                              |      |
|          `&`         |   位与运算   |                     `flags = flags & 42;`                    |  可重载 |
|       **第十二级别**      |          |                                                              |      |
|          `^`         |   位异或运算  |                     `flags = flags ^ 42;`                    |  可重载 |
|       **第十三级别**      |          |                                                              |      |
|          `|`         |   位或运算   |                     `flags = flags | 42;`                    |  可重载 |
|       **第十四级别**      |          |                                                              |      |
|         `&&`         |   逻辑与运算  |              `if (conditionA && conditionB) ...`             |  可重载 |
|   **第十五级别**         |          |                                                              |      |
|         `||`         |   逻辑或运算  |              `if (conditionA || conditionB) ...`             |  可重载 |
|   **第十六级别** （从右向左结合） |          |                                                              |      |
|         `? :`        |   条件运算符  |                   `int i = a > b ? a : b;`                   | 不可重载 |
|        `throw`       |   异常抛出   |                  `throw EClass("Message");`                  | 不可重载 |
|          `=`         |    赋值    |                         `int a = b;`                         |  可重载 |
|         `+=`         |   加赋值运算  |                           `a += 3;`                          |  可重载 |
|         `-=`         |   减赋值运算  |                           `b -= 4;`                          |  可重载 |
|         `*=`         |   乘赋值运算  |                           `a *= 5;`                          |  可重载 |
|         `/=`         |   除赋值运算  |                           `a /= 2;`                          |  可重载 |
|         `%=`         |   模赋值运算  |                           `a %= 3;`                          |  可重载 |
|         `<<=`        |  位左移赋值运算 |                        `flags <<= 2;`                        |  可重载 |
|         `>>=`        |  位右移赋值运算 |                        `flags >>= 2;`                        |  可重载 |
|         `&=`         |  位与赋值运算  |                     `flags &= new_flags;`                    |  可重载 |
|         `^=`         |  位异或赋值运算 |                     `flags ^= new_flags;`                    |  可重载 |
|         `|=`         |  位或赋值运算  |                     `flags |= new_flags;`                    |  可重载 |
|       **第十七级别**      |          |                                                              |      |
|          `,`         |   逗号分隔符  |          `for (i = 0, j = 0; i < 10; i++, j++) ...`          |  可重载 |

需要注意的是，表中并未列出 `const_cast`、`static_cast`、`dynamic_cast`、`reinterpret_cast`、`typeid`、`sizeof...`、`noexcept` 及 `alignof` 等运算符，因为它们的使用形式与函数调用相同，不会出现歧义。