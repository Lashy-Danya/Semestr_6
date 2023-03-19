import numpy as np
from scipy.stats import expon, chi2

def pearson_test(data, alpha):
    """
    Реализация критерия Пирсона для проверки соответствия данных показательному распределению.
    :param data: массив данных для анализа
    :param alpha: уровень значимости
    :return: возвращает значение статистики критерия Пирсона и соответствующий p-уровень значимости
    """
    # Определяем интервалы
    k = int(1 + 3.3 * np.log10(len(data)))
    bins = np.linspace(np.min(data), np.max(data), k)

    # Вычисляем наблюдаемые частоты в каждом интервале
    oi, _ = np.histogram(data, bins=bins)
    print(oi)

    # Вычисляем ожидаемые частоты в каждом интервале
    ei = expon.pdf((bins[:-1] + bins[1:]) / 2, loc=np.min(data), scale=np.mean(data) - np.min(data))
    ei *= len(data) * (bins[1] - bins[0])
    print(ei)

    # Вычисляем значение статистики критерия Пирсона
    chi_squared = np.sum((oi - ei) ** 2 / ei)

    # Определяем количество степеней свободы и критическое значение
    df = k - 1 - 1  # p=1, т.к. это показательное распределение
    chi2_crit = chi2.ppf(1 - alpha, df)

    # Определяем p-уровень значимости
    p_value = 1 - chi2.cdf(chi_squared, df)

    return chi_squared, p_value

# Сгенерируем выборку из показательного распределения
# data = np.random.exponential(scale=2, size=1000)
# data = np.random.uniform(size=1000)
data = np.random.normal(size=1000)

# Проверим соответствие данных показательному распределению
alpha = 0.05
chi_squared, p_value = pearson_test(data, alpha)
# if chi_squared > chi2_crit:
#     print(f"Гипотеза о соответствии данных показательному распределению отвергается (χ²={chi_squared:.2f}, "
#           f"p-value={p_value:.4f}, α={alpha}).")
# else:
#     print(f"Гипотеза о соответствии данных показательному распределению принимается (χ²={chi_squared:.2f}, "
#           f"p-value={p_value:.4f}, α={alpha}).")
