import distanceFilter, emailLib, inciweb
from fire import Fire



if __name__ == "__main__":
    fires = inciweb.getFires()

    for fire in fires:
        print(fire)