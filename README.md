# 概述
开发基于BRSM注意力机制和GhostNet轻量主干网络改进的YOLOv7算法，相比于YOLOv7目标检测算法，改进后算法检测速度提升8.48fps，平均精度提升6.2% 
# BRSM注意力结构图
![image](https://github.com/user-attachments/assets/33dc1da5-84fd-4b65-a47c-ace500da10d9)
# 网络结构
![image](https://github.com/user-attachments/assets/eef117ba-cc35-4a5c-a0d8-9518a2a4f306)
# 自建数据集上消融实验
![image](https://github.com/user-attachments/assets/ab7e6b36-f0a6-40af-9be5-280b43966293)
# 改进前后在VISDRINE上的结果对比
![image](https://github.com/user-attachments/assets/fa214c82-5590-4fd7-ad01-bff54b4c3b16) 
![image](https://github.com/user-attachments/assets/3f5ae580-ae0f-4810-95f4-5c17e0329ff4)
![image](https://github.com/user-attachments/assets/0c6a1af2-fafd-4633-aa72-523a0df76a43)
# 多模型在VISDRONE上的检测性能对比
![image](https://github.com/user-attachments/assets/0063299b-b98f-4a3b-b494-bc9386b15b0e)
# 结论
  通过将 YOLOv7 的骨干网络替换为 GhostNet 网络后，相比于原有的初始模型，参数量和浮点运算次数明显降低，推理速度提升了 8.84fps；单独集成 BRSM注意力模块后，尽管参数量和浮点运算次数相比于 YOLOv7-Ghost 网络有所增加，导致 FPS 降低了 3.85，但模型的准确率和召回率均得到了显著提升，平均精度均值提高了 0.106。将整个 GhostNet 网络和 BSAM 模块一起加入 YOLOv7 模型后，改进后 YOLOv7 模型的参数量和浮点运算次数都略高于仅替换 GhostNet网络的模型，推理速度相比于仅加入注意力机制的 YOLOv7-BSAM 模型提升2.43fps，但平均精度均值相比 YOLOv7-BSAM 提升了 0.003，相比 YOLOv7-Ghost提升了 0.109。消融实验的结果表明，GhostNet 主干网络与模型参数量和浮点运算次数关联性较大，替换后明显降低了模型复杂度，BRSM 注意力模块与模型的小目标检测能力有较大的关联性，引入注意力机制提升了模型的检测精度。
