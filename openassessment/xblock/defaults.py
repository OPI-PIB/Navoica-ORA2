# -*- coding: utf-8 -*-
"""Default data initializations for the XBlock, with formatting preserved."""
# pylint: disable=line-too-long

DEFAULT_PROMPT = """
    Cenzura w bibliotekach

    'Każdy z nas może pomyśleć o książce, która nie powinna wpaść w ręce żadnemu dziecku. Jednak jeśli ja mam prawo usunąć książkę, której nie lubię, z bibliotecznej półki, to takie samo prawo mają pozostali. W rezultacie znikną wszystkie książki.' --Katherine Paterson, autor

    Napisz przekonujący esej do gazety, w którym zawrzesz swoje poglądy na temat cenzury. Czy uważasz, że twórczość, która została uznana za szkodliwą (książki, dzieła muzyczne, filmy, czasopisma itp.) powinna zostać zakazana? Uargumentuj swoją opinię, przytocz przykłady ze swojego doświadczenia i obserwacji.
"""

DEFAULT_RUBRIC_CRITERIA = [
    {
        'name': "Ideas",
        'label': "Idee",
        'prompt': "Czy w odpowiedzi zawarta została jakaś myśl przewodnia (idea)?",
        'order_num': 0,
        'feedback': 'optional',
        'options': [
            {
                'order_num': 0, 'points': 0, 'name': 'Poor', 'label': 'Niedostatecznie',
                'explanation': """Uchwycenie myśli przewodniej jest problematyczne. Jest ona zbyt uboga/banalna."""
            },
            {
                'order_num': 1, 'points': 3, 'name': 'Fair', 'label': 'Dostatecznie',
                'explanation': """Myśl przewodnia została zawarta w odpowiedzi, ale się nie wyróżnia."""
            },
            {
                'order_num': 2, 'points': 5, 'name': 'Good', 'label': 'Dobrze',
                'explanation': """Myśl przewodnia została zawarta w odpowiedzi i się wyróżnia."""
            },
        ],
    },
    {
        'name': "Content",
        'label': "Treść",
        'prompt': "Oceń treść przesłanej odpowiedzi.",
        'order_num': 1,
        'options': [
            {
                'order_num': 0, 'points': 0, 'name': 'Poor', 'label': 'Niedostatecznie',
                'explanation': """Zawiera niewiele istotnych informacji, treść pozbawiona szczegółów, zbyt ogólna. Nieudana próba podejścia do tematu."""
            },
            {
                'order_num': 1, 'points': 1, 'name': 'Fair', 'label': 'Dostatecznie',
                'explanation': """Zawiera niewiele istotnych informacji i niewiele szczegółów. Został poruszony jeden/dwa aspekty tematu."""
            },
            {
                'order_num': 2, 'points': 3, 'name': 'Good', 'label': 'Dobrze',
                'explanation': """Zawiera wyczerpujące informacje i istotne szczegóły. Niektóre aspekty tematu zostały poruszone."""
            },
            {
                'order_num': 3, 'points': 3, 'name': 'Excellent', 'label': 'Bardzo dobrze',
                'explanation': """Zawiera wyczerpujące informacje i istotne szczegóły. Wszystkie aspekty tematu zostały poruszone."""
            },
        ],
    },
]

# The rubric's feedback prompt is a set of instructions letting the student
# know they can provide additional free form feedback in their assessment.
DEFAULT_RUBRIC_FEEDBACK_PROMPT = """
(Opcjonalnie) Co wyróżnia tę odpowiedź? Co zostało zrobione dobrze? Co można poprawić?
"""

# The rubric's feedback text is the default text displayed and used as
# the student's response to the feedback prompt
DEFAULT_RUBRIC_FEEDBACK_TEXT = """
Myślę, że ta odpowiedź jest...
"""

DEFAULT_EXAMPLE_ANSWER = (
    "Zastąp ten tekst własną przykładową odpowiedzią na to zadanie. "
    "Następnie po prawej stronie w Ocena odpowiedzi wybierz opcję do każdego kryterium. "
    "Studenci uczą się wzajemnego oceniania swoich prac. "
)

DEFAULT_EXAMPLE_ANSWER_2 = (
    "Zastąp ten tekst własną przykładową  "
    "odpowiedzią na to zadanie. Następnie wybierz opcje."
)

DEFAULT_STUDENT_TRAINING = {
    "name": "student-training",
    "start": None,
    "due": None,
    "examples": [
        {
            "answer": DEFAULT_EXAMPLE_ANSWER,
            "options_selected": [
                {
                    "criterion": "Ideas",
                    "option": "Fair"
                },
                {
                    "criterion": "Content",
                    "option": "Good"
                }
            ]
        },
        {
            "answer": DEFAULT_EXAMPLE_ANSWER_2,
            "options_selected": [
                {
                    "criterion": "Ideas",
                    "option": "Poor"
                },
                {
                    "criterion": "Content",
                    "option": "Good"
                }
            ]
        }
    ]
}

DEFAULT_START = "2001-01-01T00:00"
DEFAULT_DUE = "2029-01-01T00:00"

# The Default Peer Assessment is created as an example of how this XBlock can be
# configured. If no configuration is specified, this is the default assessment
# module(s) associated with the XBlock.
DEFAULT_PEER_ASSESSMENT = {
    "name": "peer-assessment",
    "start": DEFAULT_START,
    "due": DEFAULT_DUE,
    "must_grade": 5,
    "must_be_graded_by": 3,
}

DEFAULT_SELF_ASSESSMENT = {
    "name": "self-assessment",
    "start": DEFAULT_START,
    "due": DEFAULT_DUE,
}

DEFAULT_STAFF_ASSESSMENT = {
    "name": "staff-assessment",
    "start": DEFAULT_START,
    "due": DEFAULT_DUE,
    "required": False,
}

DEFAULT_ASSESSMENT_MODULES = [
    DEFAULT_STUDENT_TRAINING,
    DEFAULT_PEER_ASSESSMENT,
    DEFAULT_SELF_ASSESSMENT,
    DEFAULT_STAFF_ASSESSMENT,
]

DEFAULT_EDITOR_ASSESSMENTS_ORDER = [
    "student-training",
    "peer-assessment",
    "self-assessment",
    "staff-assessment",
]
