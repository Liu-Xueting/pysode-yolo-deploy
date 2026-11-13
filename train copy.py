import sys

from ultralytics.models.yolo import YOLO


def main():
    if len(sys.argv) < 2:
        print("Usage: python train.py <data_path>")
        sys.exit(1)

    model = YOLO("best.pt")
    data_path = sys.argv[1]
    results = model.train(
        data=data_path,
        epochs=50,  # 增量训练不需要 100 轮，30-50 即可
        imgsz=640,
        device=0,  # 强制走 GPU
        freeze=10,  # 【核心】冻结骨干网络，保护旧特征
        lr0=0.001,  # 【核心】低学习率，防止新数据把旧参数冲垮
        verbose=True,
        plots=True,
    )
    print(results)


if __name__ == "__main__":
    main()
