import statistics
import matplotlib.pyplot as plt


contestWeights = [420, 385, 510, 470, 450, 355, 495, 450, 410, 480, 450, 610]


def calculateMean(weights):
    return statistics.mean(weights)


def calculateMedian(weights):
    return statistics.median(weights)


def calculateMode(weights):
    return statistics.mode(weights)


def calculateStandardDeviation(weights):
    return statistics.pstdev(weights)


def calculateCoefficientOfVariation(weights):
    return calculateStandardDeviation(weights) / calculateMean(weights) * 100


def findHeaviest(weights):
    return max(weights)


def findLightest(weights):
    return min(weights)


def countInRange(weights, lowerBound, upperBound):
    return len([weight for weight in weights if lowerBound <= weight <= upperBound])


def buildStatisticsReport(weights, lowerBound, upperBound):
    return {
        "count": len(weights),
        "mean": calculateMean(weights),
        "median": calculateMedian(weights),
        "mode": calculateMode(weights),
        "standardDeviation": calculateStandardDeviation(weights),
        "coefficientOfVariation": calculateCoefficientOfVariation(weights),
        "heaviest": findHeaviest(weights),
        "lightest": findLightest(weights),
        "idealCount": countInRange(weights, lowerBound, upperBound),
        "lowerBound": lowerBound,
        "upperBound": upperBound,
    }


def describeHomogeneity(coefficientOfVariation):
    if coefficientOfVariation < 10:
        return "✨ Cultivo muy homogéneo: aguacates casi idénticos."
    if coefficientOfVariation < 20:
        return "👍 Cultivo bastante homogéneo, con alguna excepción."
    return "🎲 Cultivo heterogéneo: hay mucha variación de tamaños."


def displayReport(report):
    print("🥑" * 16)
    print("   CONCURSO DEL AGUACATE GIGANTE")
    print("🥑" * 16)
    print(f"🔢 Aguacates analizados   : {report['count']}")
    print(f"⚖️  Peso medio            : {report['mean']:.2f} g")
    print(f"📏 Peso mediano           : {report['median']:.2f} g")
    print(f"🔁 Peso más repetido      : {report['mode']} g")
    print(f"📊 Desviación estándar    : {report['standardDeviation']:.2f} g")
    print(f"📈 Coef. de variación     : {report['coefficientOfVariation']:.2f} %")
    print(f"🏆 Más pesado             : {report['heaviest']} g")
    print(f"🪶 Más ligero             : {report['lightest']} g")
    print(f"🎯 En rango {report['lowerBound']:.0f}-{report['upperBound']:.0f} g   : {report['idealCount']} aguacates")
    print(describeHomogeneity(report["coefficientOfVariation"]))
    print("🥑" * 16)


def plotDistribution(weights, lowerBound, upperBound):
    figure, (histogramAxis, boxplotAxis) = plt.subplots(1, 2, figsize=(11, 4))
    histogramAxis.hist(weights, bins=6, edgecolor="black", color="mediumseagreen")
    histogramAxis.axvline(lowerBound, color="red", linestyle="--")
    histogramAxis.axvline(upperBound, color="red", linestyle="--")
    histogramAxis.set_title("Distribución de pesos")
    histogramAxis.set_xlabel("Peso (g)")
    histogramAxis.set_ylabel("Número de aguacates")
    boxplotAxis.boxplot(weights)
    boxplotAxis.set_title("Boxplot (valores atípicos)")
    boxplotAxis.set_ylabel("Peso (g)")
    plt.tight_layout()
    plt.show()


def readWeightsFromUser():
    rawInput = input("Introduce los pesos en gramos separados por comas: ")
    return [float(piece.strip()) for piece in rawInput.split(",") if piece.strip()]


def wantsCustomWeights():
    answer = input("¿Quieres introducir tus propios aguacates? (s/n): ")
    return answer.strip().lower() == "s"


def resolveWeights():
    if wantsCustomWeights():
        return readWeightsFromUser()
    return contestWeights


def readNumber(prompt):
    return float(input(prompt).strip())


def resolveIdealRange():
    lowerBound = readNumber("Define el peso mínimo del rango ideal (g): ")
    upperBound = readNumber("Define el peso máximo del rango ideal (g): ")
    return lowerBound, upperBound


def main():
    weights = resolveWeights()
    lowerBound, upperBound = resolveIdealRange()
    report = buildStatisticsReport(weights, lowerBound, upperBound)
    displayReport(report)
    plotDistribution(weights, lowerBound, upperBound)


if __name__ == "__main__":
    main()