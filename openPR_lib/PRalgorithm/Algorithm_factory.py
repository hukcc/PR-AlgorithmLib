import fisher
import K_Nearest_Neighbor

class Algorithm_factory():
    def __init__(self, Algorithm_name):
        if Algorithm_name == "fisher":
            self.fisher()
        elif Algorithm_name == "K_Nearest_Neighbor":
            self.K_Nearest_Neighbor()
            else:
                print("we do not have that Algorithm now !")

    def fisher():
        pass

    def K_Nearest_Neighbor():
        pass