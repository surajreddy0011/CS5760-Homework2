# Q5: precision / recall from a multi-class confusion matrix
classes = ["Cat", "Dog", "Rabbit"]
cm = [[5, 10, 5],
      [15, 20, 10],
      [0, 15, 10]]

n = len(classes)
precisions, recalls = [], []
total_tp = 0

for i in range(n):
    tp = cm[i][i]                                  # correct predictions
    predicted = sum(cm[i])                         # row sum = predicted as class i
    actual = sum(cm[r][i] for r in range(n))       
    p = tp / predicted if predicted else 0
    r = tp / actual if actual else 0
    precisions.append(p)
    recalls.append(r)
    total_tp += tp
    print(f"{classes[i]}: Precision = {p:.3f}, Recall = {r:.3f}")

# macro = average of per-class scores
print(f"Macro Precision = {sum(precisions)/n:.3f}")
print(f"Macro Recall    = {sum(recalls)/n:.3f}")

# micro = pool all counts (total TP / total items)
total = sum(sum(row) for row in cm)
print(f"Micro Precision = {total_tp/total:.3f}")
print(f"Micro Recall    = {total_tp/total:.3f}")
