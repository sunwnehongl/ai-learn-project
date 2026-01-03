## Series的属性

| 属性名称|描述| 示例                                |
|------|------|-----------------------------------|
| `values` | 以NumPy数组的形式返回Series中的数据 | `s.values`                        |
| `index` | 返回Series的索引对象 | `s.index`                         |
| `dtype` | 返回Series的数据类型 | `s.dtype`                         |
| `shape` | 返回一个表示Series维度的元组 | `s.shape`                         |
| `size` | 返回Series中元素的个数 | `s.size`                          |
| `name` | 返回Series的名称 | `s.name`                          |
| `nbytes` | 返回Series数据占用的字节数 | `s.nbytes`                        |
| `ndim` | 返回Series的维度数，总是1 | `s.ndim`                          |
| `T` | 返回Series的转置（即本身） | `s.T`                             |
| `empty` | 返回Series是否为空 | `s.empty`                         |
| `hasnans` | 返回Series中是否包含NaN值 | `s.hasnans`                       |
| `is_monotonic_increasing` | 返回索引是否单调递增 | `s.index.is_monotonic_increasing` |
| `is_monotonic_decreasing` | 返回索引是否单调递减 | `s.index.is_monotonic_decreasing` |
| `is_unique` | 返回索引是否唯一 | `s.index.is_unique`               |
