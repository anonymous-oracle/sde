def hinge_loss(y_pred, y_true):
    return max(0, 1 - y_true * y_pred)

def batch_hinge_loss(y_preds, y_trues):
    return sum([hinge_loss(y_pred, y_true) for y_pred, y_true in zip(y_preds, y_trues)]) / len(y_preds)