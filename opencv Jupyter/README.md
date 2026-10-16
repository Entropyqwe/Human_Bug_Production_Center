# OpenCV 学习项目

## 目录结构

- `notebooks/`：跟着课程逐单元学习和查看中间结果。
- `scripts/`：整理后的完整 Python 程序，可从头到尾运行。
- `data/`：输入图片、视频和测试数据。
- `results/`：程序生成的输出结果。
- `cpp/`：C++ OpenCV 示例。
- `docs/`：课程笔记和依赖清单。
- `tools/`：Jupyter 启动和停止工具。
- `archive_original/`：整理前的原目录备份，不参与运行。

## 运行环境

解释器：`D:\anaconda\envs\opencv-course\python.exe`

VS Code 右上角的 Notebook 内核请选择 `Python (OpenCV Course)`。

## 学习和整理流程

1. 在 `notebooks/` 中逐格学习、运行和观察结果。
2. 确认代码正确后，将核心逻辑整理到 `scripts/` 对应的 `.py` 文件。
3. Notebook 可以使用 `%matplotlib inline`；普通 `.py` 文件删除它并使用 `plt.show()`。
4. 图片路径使用 `Path` 或 `r"..."`，中文路径使用 `np.fromfile` 加 `cv2.imdecode`。
5. 图片放入 `data/`，输出保存到 `results/`，不要把输出文件混在源代码目录。

原文件已备份到 `archive_original/`，没有删除任何学习材料。
