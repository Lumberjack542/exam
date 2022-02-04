from classTomato import Tomato
from classTomatoBush import TomatoBush
from classGarden import Garden

if __name__ == "__main__":
    Garden.knowledge_base()
    objects_of_tomato_bush = TomatoBush(8)
    objects_of_garden = Garden(1, objects_of_tomato_bush)

    objects_of_garden.work()
    objects_of_garden.harvest()





