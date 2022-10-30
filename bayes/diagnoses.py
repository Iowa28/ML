import pandas as pd
import numpy as np


def read_csv(filename):
    return pd.read_csv(filename, sep = ';')


if __name__ == '__main__':
    diseases = read_csv("disease.csv")
    diseases.set_index('disease')
    total = diseases.loc[9][1]
    # print(total)
    diseases.drop(labels = diseases.tail(1).index, inplace = True)
    diseases['prob'] = diseases['количество пациентов'] / total
    # print(diseases)

    symptoms = read_csv("symptom.csv")
    # print(symptoms)

    rand = np.random.randint(0, 2, symptoms.shape[0])
    print(rand)

    diseases_probs  = np.ones(diseases.shape[0])
    for i in range(len(diseases_probs)):
        for j in range(len(rand)):
            if rand[j] != 0:
                diseases_probs[i] *= symptoms.loc[j][i + 1]
        diseases_probs *= diseases.prob.loc[i]

    print(diseases_probs)
    disease_index = np.argmax(diseases_probs)
    print(diseases.loc[disease_index][0])