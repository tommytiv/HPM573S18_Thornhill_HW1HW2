# HUI-3 scoring formula
coefficient = 1.371
constant = 0.371
dictCoefficients = {'Vision':           [1, 0.98, 0.89, 0.84, 0.75, 0.61],
                    'Hearing':          [1, 0.95, 0.89, 0.80, 0.74, 0.61],
                    'Speech':           [1, 0.94, 0.89, 0.81, 0.68],
                    'Ambulation':       [1, 0.93, 0.86, 0.73, 0.65, 0.58],
                    'Dexterity':        [1, 0.95, 0.88, 0.76, 0.65, 0.56],
                    'Emotion':          [1, 0.95, 0.85, 0.64, 0.46],
                    'Cognition':        [1, 0.92, 0.95, 0.83, 0.60, 0.42],
                    'Pain':             [1, 0.96, 0.90, 0.77, 0.55]}


def get_score(vision: object, hearing: object, speech: object, ambulation: object, dexterity: object, emotion: object, cognition: object, pain: object) -> object:
    """

    :param vision:
    :param hearing:
    :param speech:
    :param ambulation:
    :param dexterity:
    :param emotion:
    :param cognition:
    :param pain:
    :return:
    """
    if not (vision in [1,2,3,4,5,6]):
        raise ValueError("Vision level can only take 1, 2, 3, 4, 5, or 6")

    if not (hearing in [1,2,3,4,5,6]):
       raise ValueError("Hearing level can only take 1, 2, 3, 4, 5, or 6")

    if not (speech in [1,2,3,4,5]):
       raise ValueError("Speech level can only take 1, 2, 3, 4, or 5")

    if not (ambulation in [1,2,3,4,5,6]):
       raise ValueError("Ambulation level can only take 1, 2, 3, 4, 5, or 6")

    if not (dexterity in [1,2,3,4,5,6]):
      raise ValueError("Dexterity level can only take 1, 2, 3, 4, 5, or 6")

    if not (emotion in [1,2,3,4,5]):
      raise ValueError("Emotion level can only take 1, 2, 3, 4, or 5")

    if not (cognition in [1,2,3,4,5,6]):
      raise ValueError("Cognition level can only take 1, 2, 3, 4, 5, or 6")

    if not (pain in [1,2,3,4,5]):
      raise ValueError("Pain level can only take 1, 2, 3, 4, or 5")

    response_calc = 1
    response_calc *= dictCoefficients['Vision'][vision-1]
    response_calc *= dictCoefficients['Hearing'][hearing-1]
    response_calc *= dictCoefficients['Speech'][speech-1]
    response_calc *= dictCoefficients['Ambulation'][ambulation-1]
    response_calc *= dictCoefficients['Dexterity'][dexterity-1]
    response_calc *= dictCoefficients['Emotion'][emotion-1]
    response_calc *= dictCoefficients['Cognition'][cognition-1]
    response_calc *= dictCoefficients['Pain'][pain-1]

    score = coefficient * response_calc - constant

    return score
