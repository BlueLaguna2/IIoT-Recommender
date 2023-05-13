import pandas as pd
import numpy
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from plantuml import PlantUML

plantuml = PlantUML(url='http://www.plantuml.com/plantuml/img/')
import Create_ClassFactory as ClassFactory

def CreateClassDiagram(WHname, bolPallet, bolProduct):
    UMLVariable = ""
    UMLVariable = "\n" + "@startuml\n"
    if bolPallet:
        UMLVariable = UMLVariable + "Warehouse <|-- Pallets\n"

    if bolProduct:
        UMLVariable = UMLVariable + "Pallets <|-- Products\n"

    UMLVariable = UMLVariable + "class Warehouse {\n"
    UMLVariable = UMLVariable + "    +location: string\n"
    UMLVariable = UMLVariable + "    +check_stock(product_name: string): int\n"
    UMLVariable = UMLVariable + "    }\n"
    UMLVariable = UMLVariable + "    \n"

    if bolPallet:
        UMLVariable = UMLVariable + "class Pallets {\n"
        UMLVariable = UMLVariable + "    +location: string\n"
        UMLVariable = UMLVariable + "    +pallet: string\n"
        UMLVariable = UMLVariable + "    +add_pallet(pallet_id: string, product_name: string, quantity: int): string\n"
        UMLVariable = UMLVariable + "    +remove_pallet(pallet_id: string): string\n"
        UMLVariable = UMLVariable + "    }\n"
        UMLVariable = UMLVariable + "    \n"

    if bolProduct:
        UMLVariable = UMLVariable + "class Products {\n"
        UMLVariable = UMLVariable + "    +pallet: string\n"
        UMLVariable = UMLVariable + "   +product: string\n"
        UMLVariable = UMLVariable + "   +add_product(product_name: string, quantity: int): string\n"
        UMLVariable = UMLVariable + "    +remove_product(product_name: string, quantity: int): string\n"
        UMLVariable = UMLVariable + "    }\n"
        UMLVariable = UMLVariable + "@enduml\n"

    diagram = (UMLVariable)

    image = plantuml.processes(diagram)
    with open(WHname + "_WarehouseClass.png", "wb") as f:
        f.write(image)

def ProcessInputData():
    excelFileName = "IIoT readiness Assessment.xlsx"
    dfsurveyResults = pd.read_excel(excelFileName, sheet_name="Sheet1", usecols="A, F:N", skiprows=0,
                                    names=['ID', 'WHouse', 'Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8'])

    # print(dfsurveyResults)

    for row in dfsurveyResults.index:
        WHname = ""
        Choice = 0
        Totalpts = 0
        NotMature = False
        for col in dfsurveyResults.columns:
            # extract the first character of each element in the column as survey has Choice Number prefixing the Answer chooses

            if (col != 'ID') and (col != 'Q7'):
                if (col == 'WHouse'):
                    WHname = str(dfsurveyResults.loc[row, col])
                elif (col == 'Q1'):
                    Choice = int(str(dfsurveyResults.loc[row, col])[0]) * 10
                elif (col == 'Q2'):
                    Choice = int(str(dfsurveyResults.loc[row, col])[0]) * 10
                elif (col == 'Q3'):
                    if int(str(dfsurveyResults.loc[row, col])[0]) == 1:
                        NotMature = True
                    Choice = int(str(dfsurveyResults.loc[row, col])[0]) * 50
                elif (col == 'Q4'):
                    if int(str(dfsurveyResults.loc[row, col])[0]) == 1:
                        NotMature = True
                    Choice = int(str(dfsurveyResults.loc[row, col])[0]) * 40
                elif (col == 'Q5'):
                    Choice = int(str(dfsurveyResults.loc[row, col])[0]) * 40
                elif (col == 'Q6'):
                    Choice = int(str(dfsurveyResults.loc[row, col])[0]) * 10
                elif (col == 'Q8'):
                    bolPallet = False
                    bolProduct = False
                    if pd.isna(dfsurveyResults.loc[row, col]):
                        continue
                    else:
                        matches = []
                        sentence = dfsurveyResults.loc[row, col].lower()
                        tokens = word_tokenize(sentence)
                        search_words = ['product','products']
                        matches = [word for word in tokens if word in search_words]

                       # if 'Product' in dfsurveyResults.loc[row, col]:
                        if (not pd.isna(matches) and matches != []):
                            bolProduct = True
                        else:
                            bolProduct = False

                        matches = []
                        sentence = dfsurveyResults.loc[row, col].lower()
                        tokens = word_tokenize(sentence)
                        search_words = ['pallet','pallets']
                        matches = [word for word in tokens if word in search_words]
                        if (not pd.isna(matches) and matches != []):
                            bolPallet= True
                        else:
                            bolPallet = False
                Totalpts += Choice
            # print(str(col), ' ', str(dfsurveyResults.loc[row, col])[0])
        PrintResults(Totalpts, NotMature, bolPallet, bolProduct,WHname)
        CreateClassDiagram(WHname, bolPallet, bolProduct)

def PrintResults(Totalpts, NotMature, bolPallet, bolProduct,WHname):
    print()
    print('Total Calculated pts = ' + str(Totalpts))

    if NotMature == True:
        print('Warehouse needs to get IT systems and/or Network upgrade.')
    elif Totalpts <= 260:  # Maturity Level 1
        print('Warehouse ' + WHname + ' is at Maturity Level 1 and could begin with Barcode scanning with affixed labels to the Product/container.')
        ClassFactory.CreateWarehouseClassFactory(bolPallet, bolProduct,WHname)
    elif Totalpts <= 360:  # Maturity Level 2
        print('Warehouse ' + WHname + ' is at Maturity Level 2 and could begin with a mix of RFDT tags or Barcode scanning with labels affixed to the Product/container.')
        ClassFactory.CreateWarehouseClassFactory(bolPallet, bolProduct,WHname)
    elif Totalpts <= 470:  # Maturity Level 3
        print('Warehouse ' + WHname + ' is at Maturity Level 3 and could begin with a mix of IIOT devices or RFDT tags attached to the Product/container.')
        ClassFactory.CreateWarehouseClassFactory(bolPallet, bolProduct,WHname)
    elif Totalpts <= 580:  # Maturity Level 4
        print('Warehouse ' + WHname + ' is at Maturity Level 4 and could begin using IIOT devices to trace movement of your Product/container.')
        ClassFactory.CreateWarehouseClassFactory(bolPallet, bolProduct,WHname)
    else:  # Maturity Level 5
        print('Warehouse ' + WHname + ' is at Maturity Level 5 and should aim to become I4.0 compliant.')
        ClassFactory.CreateWarehouseClassFactory(bolPallet, bolProduct,WHname)

    print()
    print('========================================================================================')

if __name__ == '__main__':
    ProcessInputData()