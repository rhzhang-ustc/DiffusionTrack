def bbox_xywh2xyxy(bbox):
    return (bbox[0], bbox[1], bbox[2] + bbox[0] - 1, bbox[3] + bbox[1] - 1)
