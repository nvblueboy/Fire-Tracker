import distanceFilter, emailLib, inciweb
from fire import Fire



if __name__ == "__main__":
    fires = inciweb.getFires()

    filteredFires = distanceFilter.filter(fires)

    for fire in filteredFires:
        print(fire)