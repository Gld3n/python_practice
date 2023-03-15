class JobOffer:
    def __init__(self, offer_name:str, description:str, level="Junior", salary=5_000) -> None:
        self.offer_name = offer_name
        self.level = level
        self.description = description
        self.salary = salary
        
    def job_info(self):
        info = f"""
        ================================
        {self.offer_name} - {self.level}
                                        
        Job description:                
        {self.description}        
        --------------------------------
        Salary: {self.salary}$                    
        ================================
        """
        return info

class JobOffers:
    offers = []
    n_offers = 0
    
    def __init__(self) -> None:
        JobOffers.get_offers()
    
    @classmethod
    def add_offer(cls, job_offer:JobOffer) -> None:
        cls.offers.append(job_offer)
        cls.n_offers += 1
        
    @classmethod
    def get_offers(cls) -> None:
        print("These are the current job offers:")
        for o in cls.offers:
            if o == cls.offers[-1]:
                try:
                    print(o.offer_name, end=".")
                except AttributeError:
                    print(o, end=".")
            else:
                try:
                    print(o.offer_name, end=", ")
                except AttributeError:
                    print(o, end=", ")

programmer_offer = JobOffer(
    "Programmer",
    "Someone who bathes cats.",
    salary = 5_000
)
print(programmer_offer.job_info())

psychologist_offer = JobOffer(
    "Psychologist",
    "Someone who kills robots.",
    level = "Senior",
    salary = 50_000
)

JobOffers.add_offer(programmer_offer)
JobOffers.add_offer("Surgeon")
JobOffers.add_offer(psychologist_offer)
JobOffers.add_offer("Nutricionist")
JobOffers.add_offer("Attorney")

# print(JobOffers.offers)
# print(JobOffers.n_offers)
JobOffers.get_offers()