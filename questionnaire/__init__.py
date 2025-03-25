from otree.api import *
import random
import itertools


doc = """
Questionnaire
"""


class C(BaseConstants):
    NAME_IN_URL = "questionnaire"
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


def creating_session(subsession):
    order_blocks = itertools.cycle(subsession.session.config["blocks"])
    for p in subsession.get_players():
        p.order_blocks = next(order_blocks)
        p.orderB = random.choice(subsession.session.config["orderB"])


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    id_cint = models.StringField()
    order_blocks = models.StringField()
    orderB = models.IntegerField()

    gender = models.StringField(
        label="¿Eres hombre o mujer?", choices=["Hombre", "Mujer"]
    )

    age = models.IntegerField(label="¿Qué edad tienes?", min=18, max=100)

    marital_status = models.IntegerField(
        label="¿Actualmente...",
        choices=[
            [1, "Vives con tu pareja en unión libre"],
            [2, "Estás separado"],
            [3, "Estás divorciado"],
            [4, "Eres viudo"],
            [5, "Estás casado: sólo por el civil"],
            [6, "Estás casado: sólo por la iglesia"],
            [7, "Estás casado: civil y por la iglesia"],
            [8, "Estás soltero"],
        ],
    )

    birth_place = models.IntegerField(
        label="¿En qué estado de la República o en qué país naciste?",
        choices=[
            [1, "Aguascalientes"],
            [2, "Baja California"],
            [3, "Baja California Sur"],
            [4, "Campeche"],
            [5, "Coahuila de Zaragoza"],
            [6, "Colima"],
            [7, "Chiapas"],
            [8, "Chihuahua"],
            [9, "Ciudad de México"],
            [10, "Durango"],
            [11, "Guanajuato"],
            [12, "Guerrero"],
            [13, "Hidalgo"],
            [14, "Jalisco"],
            [15, "México"],
            [16, "Michoacán de Ocampo"],
            [17, "Morelos"],
            [18, "Nayarit"],
            [19, "Nuevo León"],
            [20, "Oaxaca"],
            [21, "Puebla"],
            [22, "Querétaro"],
            [23, "Quintana Roo"],
            [24, "San Luis Potosí"],
            [25, "Sinaloa"],
            [26, "Sonora"],
            [27, "Tabasco"],
            [28, "Tamaulipas"],
            [29, "Tlaxcala"],
            [30, "Veracruz de Ignacio de la Llave"],
            [31, "Yucatán"],
            [32, "Zacatecas"],
            [98, "En los Estados Unidos de América"],
            [99, "En otro país"],
        ],
    )

    living_area = models.IntegerField(
        label="¿Vives en una ciudad o en una zona rural?",
        choices=[[1, "Ciudad"], [2, "Pueblo"], [3, "Zona rural"]],
    )

    education_level = models.IntegerField(
        label="¿Cuál es el nivel de estudios más alto alcanzado?",
        choices=[
            [0, "Ninguno"],
            [1, "Preescolar"],
            [2, "Primaria"],
            [3, "Secundaria"],
            [4, "Preparatoria o bachillerato general"],
            [5, "Bachillerato tecnológico"],
            [6, "Estudios técnicos o comerciales con primaria terminada"],
            [7, "Estudios técnicos o comerciales con secundaria terminada"],
            [8, "Estudios técnicos o comerciales con preparatoria terminada"],
            [9, "Normal con primaria o secundaria terminada"],
            [10, "Normal de licenciatura"],
            [11, "Licenciatura"],
            [12, "Especialidad"],
            [13, "Maestría"],
            [14, "Doctorado"],
        ],
    )

    education_grade = models.IntegerField(
        label="¿Cuál fue el último año o grado que aprobaste en la escuela?"
    )

    currently_studying = models.IntegerField(
        label="¿Estás estudiando actualmente?", choices=[[1, "Sí"], [2, "No"]]
    )

    employment_status = models.IntegerField(
        label="Ahora te voy a preguntar por la situación laboral.\n¿La semana pasada:",
        choices=[
            [1, "Trabajaste (por lo menos una hora)"],
            [2, "Tenías trabajo, pero no trabajaste"],
            [3, "Buscaste trabajo"],
            [4, "Estás pensionada(o) o jubilada(o)"],
            [5, "Eres estudiante"],
            [6, "Te dedicas a los quehaceres de tu hogar"],
            [
                7,
                "Tienes alguna limitación física o mental permanente que te impide trabajar",
            ],
            [8, "Estabas en otra situación diferente a las anteriores"],
        ],
    )

    occupation_last_week = models.IntegerField(
        label="¿Cuál fue tu ocupación la semana pasada?",
        choices=[
            [1, "Funcionario, director o jefe"],
            [2, "Profesionista o técnico"],
            [3, "Trabajador auxiliar en actividades administrativas"],
            [4, "Comerciante, empleado en ventas o agente de ventas"],
            [5, "Trabajador en servicios personales y de vigilancia"],
            [
                6,
                "Trabajador en actividades agrícolas, ganaderas, forestales, caza y pesca",
            ],
            [7, "Trabajador artesanal, en la construcción y otros oficios"],
            [
                8,
                "Operador de maquinaria industrial, ensamblador, chofer o conductor de transporte",
            ],
            [9, "Trabajador en actividades elementales y de apoyo"],
            [10, "Ninguna"]
        ],
        blank=True,
    )

    emigrated_since_2020 = models.IntegerField(
        label="¿Has emigrado fuera de México por 3 meses o más después de marzo de 2020?",
        choices=[[1, "Sí"], [2, "No"]],
    )

    family_emigrated_to_us = models.IntegerField(
        label="¿Tienes algún familiar que haya emigrado a Estados Unidos en los últimos 5 años?",
        choices=[[1, "Sí"], [2, "No"]],
    )

    attention_check = models.IntegerField(
        label="En cuestionarios como el nuestro, a veces hay participantes que no leen atentamente las preguntas. Esto significa que muchas respuestas podrían comprometer los resultados de los estudios de investigación. Para demostrar que has leído atentamente, respuesta a la siguiente pregunta.\nLas rayas de la bandera estadounidense son rojas y ¿de qué otro color?",
        choices=[
            [1, "Verde"],
            [2, "Amarillo"],
            [3, "Azul"],
            [4, "Naranja"],
            [5, "Rosa"],
            [6, "Morado"],
            [7, "Turquesa"],
            [8, "Negro"],
            [9, "Blanco"],
        ],
    )

    probability_marriage_mex = models.IntegerField(
        label="¿Qué probabilidad crees que tendrás de casarte (o vivir en unión libre) dentro de 10 años?",
        choices=[
            [1, "Extremadamente improbable (<20% de probabilidad)"],
            [2, "Improbable (20-39% de probabilidad)"],
            [3, "Neutro (40-59% de probabilidad)"],
            [4, "Probable (60-79% de probabilidad)"],
            [5, "Extremadamente probable (>=80% de probabilidad)"],
        ],
    )

    spouse_age_mex = models.IntegerField(
        label="En cuanto a la edad, ¿crees que tu cónyuge/pareja tendrá",
        choices=[
            [1, "Por lo menos 3 años menos que tú"],
            [2, "Aproximadamente la misma edad, más o menos 2 años"],
            [3, "Por lo menos 3 años más que tú"],
            [4, "No sabrías decirlo"],
        ],
    )

    spouse_birthplace_mex = models.IntegerField(
        label="En cuanto al lugar de nacimiento, ¿crees que tu cónyuge/pareja",
        choices=[
            [1, "Nacerá en el mismo estado mexicano que tú"],
            [2, "Nacerá en otro estado mexicano"],
            [3, "Nacerá en otro país"],
            [4, "No sabrías decirlo"],
        ],
    )

    spouse_education_mex = models.IntegerField(
        label="En términos de educación, ¿crees que en el momento de casarte tu cónyuge/pareja en unión libre tendrá:",
        choices=[
            [1, "El mismo nivel de educación que tú tendrás"],
            [2, "Un nivel de educación menor que el que tú tendrás"],
            [3, "Un nivel de educación mayor que el que tú tendrás"],
            [4, "No sabrías decirlo"],
        ],
    )

    spouse_characteristics_mex = models.IntegerField(
        label="En cuanto a otras características que puedas pensar (como el origen cultural, el trabajo, otras...), cuando intentas visualizar a tu futuro cónyuge/pareja, la imagen mental que tienes es:",
        choices=[
            [1, "Muy incierta"],
            [2, "Incierta"],
            [3, "Bastante incierta"],
            [4, "Bastante segura"],
            [5, "Segura"],
        ],
    )

    probability_marriage_us = models.IntegerField(
        label="¿Qué probabilidad crees que tendrás de casarte (o vivir en unión libre) dentro de 10 años?",
        choices=[
            [1, "Extremadamente improbable (<20% de probabilidad)"],
            [2, "Improbable (20-39% de probabilidad)"],
            [3, "Neutro (40-59% de probabilidad)"],
            [4, "Probable (60-79% de probabilidad)"],
            [5, "Extremadamente probable (>=80% de probabilidad)"],
        ],
    )

    spouse_age_us = models.IntegerField(
        label="En cuanto a la edad, ¿crees que tu cónyuge/pareja tendrá",
        choices=[
            [1, "Por lo menos 3 años menos que tú"],
            [2, "Aproximadamente la misma edad, más o menos 2 años"],
            [3, "Por lo menos 3 años más que tú"],
            [4, "No sabrías decirlo"],
        ],
    )

    spouse_birthplace_us = models.IntegerField(
        label="En cuanto al lugar de nacimiento, ¿crees que tu cónyuge/pareja",
        choices=[
            [1, "Nacerá en el mismo estado mexicano que tú"],
            [2, "Nacerá en otro estado mexicano"],
            [3, "Nacerá en otro país"],
            [4, "No sabrías decirlo"],
        ],
    )

    spouse_education_us = models.IntegerField(
        label="En términos de educación, ¿crees que en el momento de casarte tu cónyuge/pareja en unión libre tendrá:",
        choices=[
            [1, "El mismo nivel de educación que tú tendrás"],
            [2, "Un nivel de educación menor que el que tú tendrás"],
            [3, "Un nivel de educación mayor que el que tú tendrás"],
            [4, "No sabrías decirlo"],
        ],
    )

    spouse_characteristics_us = models.IntegerField(
        label="En cuanto a otras características que puedas pensar (como el origen cultural, el trabajo, otras...), cuando intentas visualizar a tu futuro cónyuge/pareja, la imagen mental que tienes es:",
        choices=[
            [1, "Muy incierta"],
            [2, "Incierta"],
            [3, "Bastante incierta"],
            [4, "Bastante segura"],
            [5, "Segura"],
        ],
    )

    visualize_spouse_scenario = models.IntegerField(
        label="Considera ahora los dos escenarios (México y Estados Unidos); trata de visualizar las características de tu futuro cónyuge/pareja en cada escenario. En caso de emigrar a Estados Unidos, ¿eres",
        choices=[
            [
                1,
                "Más capaz de visualizar estas características que en el caso de quedarte en México",
            ],
            [2, "Tan capaz como en el caso de quedarte en México"],
            [3, "Menos capaz que en el caso de quedarte en México"],
        ],
    )

    prefer_migrate_us = models.IntegerField(
        label="Idealmente, ¿preferirías migrar permanentemente a Estados Unidos o quedarte en México?",
        choices=[
            [1, "Migrar a Estados Unidos"],
            [2, "Prefieres quedarte en México"],
        ],
    )

    concrete_steps_migration = models.IntegerField(
        label="¿Has dado pasos concretos para una futura migración a Estados Unidos?",
        choices=[[1, "Sí"], [2, "No"]],
    )

    probability_migrate_us = models.IntegerField(
        label="¿Qué tan probable es que te mudes a Estados Unidos en los próximos cinco años?",
        choices=[
            [1, "Muy improbable"],
            [2, "Improbable"],
            [3, "Probable"],
            [4, "Muy probable"],
            [5, "No lo sé"],
        ],
    )

    importance_salary_difference = models.IntegerField(
        label="La diferencia de salarios que puedes ganar en los dos países",
        choices=[
            [1, "Nada importantes"],
            [2, "Algo importantes"],
            [3, "Importantes"],
            [4, "Extremadamente importantes"],
        ],
        widget=widgets.RadioSelect,
    )

    importance_professional_prospects = models.IntegerField(
        label="Las perspectivas profesionales",
        choices=[
            [1, "Nada importantes"],
            [2, "Algo importantes"],
            [3, "Importantes"],
            [4, "Extremadamente importantes"],
        ],
        widget=widgets.RadioSelect,
    )

    importance_legal_status = models.IntegerField(
        label="Tu situación legal en Estados Unidos",
        choices=[
            [1, "Nada importantes"],
            [2, "Algo importantes"],
            [3, "Importantes"],
            [4, "Extremadamente importantes"],
        ],
        widget=widgets.RadioSelect,
    )

    importance_marriage_decisions = models.IntegerField(
        label="Decisiones de matrimonio o de unión libre",
        choices=[
            [1, "Nada importantes"],
            [2, "Algo importantes"],
            [3, "Importantes"],
            [4, "Extremadamente importantes"],
        ],
        widget=widgets.RadioSelect,
    )


# PAGES
class InformedConsent(Page):

    @staticmethod
    def vars_for_template(player):
        player.id_cint = player.participant.label


class InformedConsent2(Page):
    pass


class BlockA1(Page):
    form_model = "player"
    form_fields = ["gender", "age", "marital_status"]


class Screening(Page):
    form_model = "player"

    @staticmethod
    def is_displayed(player):
        return (
            player.marital_status != 8
            or player.gender != "Hombre"
            or player.age > 25
        )

    @staticmethod
    def vars_for_template(player):
        completion_link = (
            "https://samplicio.us/s/ClientCallBack.aspx?RIS=20&RID="
            + player.participant.label
        )
        return dict(completion_link=completion_link)


class BlockA2(Page):
    form_model = "player"
    form_fields = [
        "birth_place",
        "living_area",
        "education_level",
        "education_grade",
        "currently_studying",
        "employment_status",
        "occupation_last_week",
        "emigrated_since_2020",
        "family_emigrated_to_us",
        "attention_check",
    ]


class BlockB1A(Page):
    form_model = "player"

    @staticmethod
    def get_form_fields(player):
        if player.orderB == 0:
            return [
                "probability_marriage_mex",
                "spouse_age_mex",
                "spouse_birthplace_mex",
                "spouse_education_mex",
                "spouse_characteristics_mex",
            ]
        else:
            return [
                "probability_marriage_us",
                "spouse_age_us",
                "spouse_birthplace_us",
                "spouse_education_us",
                "spouse_characteristics_us",
            ]

    @staticmethod
    def is_displayed(player):
        return player.order_blocks == "BC"


class BlockB2A(Page):
    form_model = "player"

    @staticmethod
    def get_form_fields(player):
        if player.orderB == 0:
            return [
                "probability_marriage_us",
                "spouse_age_us",
                "spouse_birthplace_us",
                "spouse_education_us",
                "spouse_characteristics_us",
            ]
        else:
            return [
                "probability_marriage_mex",
                "spouse_age_mex",
                "spouse_birthplace_mex",
                "spouse_education_mex",
                "spouse_characteristics_mex",
            ]

    @staticmethod
    def is_displayed(player):
        return player.order_blocks == "BC"


class BlockB3A(Page):
    form_model = "player"
    form_fields = ["visualize_spouse_scenario"]

    @staticmethod
    def is_displayed(player):
        return player.order_blocks == "BC"


class BlockC(Page):
    form_model = "player"
    form_fields = [
        "prefer_migrate_us",
        "concrete_steps_migration",
        "probability_migrate_us",
    ]


class BlockC1(Page):
    form_model = "player"
    form_fields = [
        "importance_salary_difference",
        "importance_professional_prospects",
        "importance_legal_status",
        "importance_marriage_decisions",
    ]



class BlockB1B(Page):
    form_model = "player"

    @staticmethod
    def get_form_fields(player):
        if player.orderB == 0:
            return [
                "probability_marriage_mex",
                "spouse_age_mex",
                "spouse_birthplace_mex",
                "spouse_education_mex",
                "spouse_characteristics_mex",
            ]
        else:
            return [
                "probability_marriage_us",
                "spouse_age_us",
                "spouse_birthplace_us",
                "spouse_education_us",
                "spouse_characteristics_us",
            ]

    @staticmethod
    def is_displayed(player):
        return player.order_blocks == "CB"


class BlockB2B(Page):
    form_model = "player"

    @staticmethod
    def get_form_fields(player):
        if player.orderB == 0:
            return [
                "probability_marriage_us",
                "spouse_age_us",
                "spouse_birthplace_us",
                "spouse_education_us",
                "spouse_characteristics_us",
            ]
        else:
            return [
                "probability_marriage_mex",
                "spouse_age_mex",
                "spouse_birthplace_mex",
                "spouse_education_mex",
                "spouse_characteristics_mex",
            ]

    @staticmethod
    def is_displayed(player):
        return player.order_blocks == "CB"


class BlockB3B(Page):
    form_model = "player"
    form_fields = ["visualize_spouse_scenario"]

    @staticmethod
    def is_displayed(player):
        return player.order_blocks == "CB"

class Completion(Page):

    @staticmethod
    def vars_for_template(player):
        completion_link = (
            "https://notch.insights.supply/cb?token=79844413-27e9-4fb3-ae67-6379f015a848&RID="
            + player.participant.label
        )
        return dict(completion_link=completion_link)


page_sequence = [
    InformedConsent,
    InformedConsent2,
    BlockA1,
    Screening,
    BlockA2,
    BlockB1A,
    BlockB2A,
    BlockB3A,
    BlockC,
    BlockC1,
    BlockB1B,
    BlockB2B,
    BlockB3B,
    Completion,
]
