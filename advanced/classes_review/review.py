import sys
sys.tracebacklimit = -1

class JobOffer:
    """Defines a structure for the job offer to be posted"""
    
    def __init__(self, offer_name:str, description:str, level="Junior", salary=5_000) -> None:
        self.offer_name = offer_name
        self.level = level
        self.description = description
        self.salary = salary
        
    def __repr__(self) -> str:
        return f"JobOffer({self.offer_name}) - This is an offer for a {self.offer_name} job."
        
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

class InvalidFormatException(Exception):
    def __init__(self, message = "Invalid format or request") -> None:
        self.message = message
        super().__init__(self.message)

class JobOffers:
    """Gathers all the job offers posted by the employees"""
    offers = []
    
    def __init__(self) -> None:
        # Demonstrative
        JobOffers.get_offers()
    
    @staticmethod
    def etiquette():
        print("\nYou must wear a shiny orange oversized suit to your interview.")
    
    @classmethod
    def add_offer(cls, job_offer:JobOffer|str) -> None:
        cls.offers.append(job_offer)
        
    @classmethod
    def get_offers(cls) -> None:
        print("These are the current job offers:")
        for o in cls.offers:
            if o == cls.offers[-1]:
                try:
                    print(o.offer_name, end=".\n")
                except AttributeError:
                    print(o, end=".\n")
            else:
                try:
                    print(o.offer_name, end=", ")
                except AttributeError:
                    print(o, end=", ")
            
    @classmethod             
    def get_info(cls, offer:JobOffer|str) -> None:
        if isinstance(offer, JobOffer) or type(offer) == str:
            if offer in cls.offers:
                try:
                    print(offer.job_info())
                except AttributeError:
                    print(f"\n{offer}")
            else:
                print("\nMaybe you've seen that offer in another job site... cheater.")
        else:
            raise InvalidFormatException


programmer_offer = JobOffer(
    "Programmer",
    "Someone who bathes cats.",
    salary = 5_000
)

psychologist_offer = JobOffer(
    "Psychologist",
    "Someone who kills robots.",
    level = "Senior",
    salary = 50_000
)