from dataclass import PersonalInformation, WorkExperience, Education, CandidateApplication
from data import data
from pydantic import ValidationError

class CandidateApplicationBuilder:
    def __init__(self):
        self.personal_info = None
        self.work_experience = []
        self.education = []

    def set_personal_info(
            self,
            first_name,
            middle_name,
            last_name,
            phone,
            location ):
        self.personal_info = PersonalInformation(
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            phone=phone,
            location=location)

    def set_work_experience(self, employer, from_date, to_date, role, is_current=False):
        self.work_experience.append(WorkExperience(
            employer=employer,
            from_date=from_date,
            to_date=to_date,
            role=role,
            is_current=is_current
        ))

    def set_education(self, institute, degree, duration):
        self.education.append(Education(
            institute=institute,
            degree=degree,
            duration=duration
        ))

    def build(self):
        return CandidateApplication(
            personal_information=self.personal_info,
            work_experience=self.work_experience,
            education=self.education
        )


# ---------- client code ----------

personal_information = data["personal_info"]
work_experience = data["work_experience"]
education = data["education"]

try:
    candidate = CandidateApplicationBuilder()
    candidate.set_personal_info(
        personal_information["first_name"],
        personal_information["middle_name"],
        personal_information["last_name"],
        personal_information["phone"],
        personal_information["location"] ,
    )
    if len(work_experience) > 0:
        for experience in work_experience:
            candidate.set_work_experience(
                experience["employer"],
                experience['from_date'],
                experience['to_date'],
                experience['role'],
                experience['is_current']
            )

    print(candidate)
except ValidationError as err:
    print(err.json(indent=2))
except Exception as e:
    print(e)


print(candidate.build())