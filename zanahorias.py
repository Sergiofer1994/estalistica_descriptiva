import statistics
import matplotlib.pyplot as plt


contestWeights = [300, 280, 290, 310, 275, 290, 295, 315, 290, 280, 310, 305]


def calculateMean(weights):
    return statistics.mean(weights)


def calculateMedian(weights):
    return statistics.median(weights)


def calculateMode(weights):
    return statistics.mode(weights)


def calculateStandardDeviation(weights):
    return statistics.pstdev(weights)


def buildStatisticsReport(weights):
    return {
        "count": len(weights),
        "mean": calculateMean(weights),
        "median": calculateMedian(weights),
        "mode": calculateMode(weights),
        "standardDeviation": calculateStandardDeviation(weights),
    }


def describeUniformity(standardDeviation):
    if standardDeviation < 10:
        return "✨ ¡Cultivo muy uniforme! Zanahorias casi clónicas."
    if standardDeviation < 20:
        return "👍 Cultivo bastante regular, con alguna zanahoria rebelde."
    return "🎲 Cultivo muy variado: hay zanahorias de todos los tamaños."


def displayReport(report):
    print("🥕" * 15)
    print("   CONCURSO DE LA ZANAHORIA GIGANTE")
    print("🥕" * 15)
    print(f"🔢 Zanahorias analizadas : {report['count']}")
    print(f"⚖️  Peso medio           : {report['mean']:.2f} g")
    print(f"📏 Peso mediano          : {report['median']:.2f} g")
    print(f"🏆 Peso más repetido     : {report['mode']} g")
    print(f"📊 Desviación estándar   : {report['standardDeviation']:.2f} g")
    print(describeUniformity(report["standardDeviation"]))
    print("🥕" * 15)


def plotDistribution(weights):
    plt.hist(weights, bins=6, edgecolor="black", color="orange")
    plt.title("Distribución del peso de las zanahorias")
    plt.xlabel("Peso (g)")
    plt.ylabel("Número de zanahorias")
    plt.tight_layout()
    plt.show()


def readCustomWeights():
    rawInput = input("Introduce los pesos en gramos separados por comas: ")
    return [float(piece.strip()) for piece in rawInput.split(",") if piece.strip()]


def wantsCustomWeights():
    answer = input("¿Quieres analizar tus propias zanahorias? (s/n): ")
    return answer.strip().lower() == "s"


def resolveWeights():
    if wantsCustomWeights():
        return readCustomWeights()
    return contestWeights


def main():
    weights = resolveWeights()
    report = buildStatisticsReport(weights)
    displayReport(report)
    plotDistribution(weights)


if __name__ == "__main__":
    main()