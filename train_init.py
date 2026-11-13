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
        epochs=50,
        imgsz=640,
        verbose=True,
        plots=True,
        # multi gpus
        device=0,
    )
    print(results)


if __name__ == "__main__":
    main()
