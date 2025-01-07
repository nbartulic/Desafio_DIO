def calcular_sensibilidade(vp, fn):
    return vp / (vp + fn) if (vp + fn) > 0 else 0

def calcular_especificidade(vn, fp):
    return vn / (fp + vn) if (fp + vn) > 0 else 0

def calcular_acuracia(vp, vn, fp, fn):
    n = vp + vn + fp + fn
    return (vp + vn) / n if n > 0 else 0

def calcular_precisao(vp, fp):
    return vp / (vp + fp) if (vp + fp) > 0 else 0

def calcular_fscore(precisao, sensibilidade):
    return 2 * (precisao * sensibilidade) / (precisao + sensibilidade) if (precisao + sensibilidade) > 0 else 0

vp = 50  # Verdadeiros Positivos
vn = 40  # Verdadeiros Negativos
fp = 10  # Falsos Positivos
fn = 20  # Falsos Negativos

sensibilidade = calcular_sensibilidade(vp, fn)
especificidade = calcular_especificidade(vn, fp)
acuracia = calcular_acuracia(vp, vn, fp, fn)
precisao = calcular_precisao(vp, fp)
fscore = calcular_fscore(precisao, sensibilidade)

print("Métricas de Avaliação do Modelo:")
print(f"Sensibilidade (Recall): {sensibilidade:.2f}")
print(f"Especificidade: {especificidade:.2f}")
print(f"Acurácia: {acuracia:.2f}")
print(f"Precisão: {precisao:.2f}")
print(f"F-score: {fscore:.2f}")
