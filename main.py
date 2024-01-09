import tkinter as tk
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk

class ServiceProvider:
    def __init__(self, name, service, contact, experience, prices, specialty):
        self.name = name
        self.service = service
        self.contact = contact
        self.experience = experience
        self.prices = prices
        self.specialty = specialty

class User:
    def __init__(self, name, address, contact):
        self.name = name
        self.address = address
        self.contact = contact

class HelpingHandProject:
    def __init__(self):
        self.service_providers = []

    def add_service_provider(self, name, service, contact, experience, prices, specialty):
        provider = ServiceProvider(
            name, service, contact, experience, prices, specialty)
        self.service_providers.append(provider)

    def find_providers_by_service(self, user_input):
        matching_providers = [
            provider for provider in self.service_providers if user_input.lower() in provider.service.lower()
        ]
        return matching_providers

class HelpingHandGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Helping Hand Project")
        self.master.configure(bg='#e6ffe6')  # Background color

        # Create a frame for better organization
        self.frame = tk.Frame(root, padx=10, pady=10)
        self.frame.pack()

        # Add a title label
        title_label = tk.Label(self.frame, text="Welcome to Helping Hand Service", font=('Helvetica', 10, 'bold'))
        title_label.grid(row=0, column=0, columnspan=10, pady=(0, 0))

        # Load the image
        image_path = "final.jpg"  # Replace with your actual image file path
        self.image = Image.open(image_path)
        self.photo = ImageTk.PhotoImage(self.image)

        # Create a label to display the image
        self.image_label = tk.Label(self.master, image=self.photo, bg='#e6ffe6')
        self.image_label.pack()

        self.helping_hand_project = HelpingHandProject()
        self.create_widgets()
        self.add_service_providers()  # Add service providers on initialization
        self.selected_services = []

    def create_widgets(self):
        # Create a frame for user details
        user_details_frame = tk.Frame(self.master, bg='#e6ffe6')  # Background color
        user_details_frame.pack(padx=10, pady=10)

        self.label_name = tk.Label(user_details_frame, text="Enter Your Name:", bg='#e6ffe6')  # Background color
        self.label_name.grid(row=0, column=0, sticky="w", pady=5)
        self.entry_name = tk.Entry(user_details_frame)
        self.entry_name.grid(row=0, column=1, pady=5)

        self.label_address = tk.Label(
            user_details_frame, text="Enter Your Address:", bg='#e6ffe6')  # Background color
        self.label_address.grid(row=1, column=0, sticky="w", pady=5)
        self.entry_address = tk.Entry(user_details_frame)
        self.entry_address.grid(row=1, column=1, pady=5)

        self.label_contact = tk.Label(
            user_details_frame, text="Enter Your Contact Number:", bg='#e6ffe6')  # Background color
        self.label_contact.grid(row=2, column=0, sticky="w", pady=5)
        self.entry_contact = tk.Entry(user_details_frame)
        self.entry_contact.grid(row=2, column=1, pady=5)

        # Improved submit button styling
        self.submit_button = tk.Button(
            self.master, text="Submit", command=self.get_user_details, bg="#660000", fg="white", font=("Arial", 12))
        self.submit_button.pack(pady=10)

    def add_service_providers(self):
        provider_data = [
            ("Ali Khan", "Plumbing", "0301-2345678", "10 years", "Rs. 500/hour", "Residential plumbing"),
            ("Saif Ahmed", "Electrician", "0312-3456789", "8 years", "Rs. 600/hour", "Commercial electrical work"),
    ("Ahmed Malik", "Carpentry", "0343-9876543", "15 years", "Rs. 400/hour", "Custom furniture and cabinets"),
    ("Zohaib Zafar", "Car Mechanic", "0333-1112222", "12 years", "Rs. 700/hour", "Auto diagnostics and repair"),
    ("Mahad Aslam", "Car Mechanic", "0322-3344556", "12 years", "Rs. 700/hour", "General automotive mechanic"),
    ("Zafar Iqbal", "Car Mechanic", "0311-2233445", "12 years", "Rs. 700/hour", "Brake and transmission technicians"),
    ("Daniyal Rashid", "Plumber", "0320-1122334", "10 years", "Rs. 550/hour", "Pipe installation and repair"),
    ("Gulab Khan", "Car Mechanic", "0344-5566778", "7 years", "Rs. 300/hour", "Auto body mechanics"),
    ("Christopher Randolph", "House Cleaning", "0311-9988776", "5 years", "Rs. 250/hour", "General house cleaning"),
    ("Usama Ali", "Painting", "0320-3344556", "8 years", "Rs. 450/hour", "Interior and exterior painting"),
    ("Haroon Khan", "Roofing", "0344-5566778", "10 years", "Rs. 600/hour", "Roof repair and installation"),
    ("Faazil Akhter", "HVAC", "0311-9988776", "12 years", "Rs. 800/hour", "Heating and air conditioning services"),
    ("Ziavish Sheikh", "Appliance Repair", "0320-1122334", "6 years", "Rs. 500/hour", "Appliance troubleshooting and repair"),
    ("Danish Ali", "Locksmith", "0344-3344556", "8 years", "Rs. 400/hour", "Lock installation and repair"),
    ("Naeem Ali", "Mechanic", "0311-5566778", "9 years", "Rs. 350/hour", "Auto glass mechanics."),
    ("Waqar Ali", "Car Detailing", "0320-9988776", "4 years", "Rs. 600/hour", "Car washing and detailing"),
    ("Shamshad Ali", "Computer Repair", "0344-1122334", "7 years", "Rs. 500/hour", "Computer troubleshooting and repair"),
    ("Zohaib Khan", "Graphic Design", "0311-3344556", "5 years", "Rs. 450/hour", "Graphic design services"),
    ("Khawar Jokhio", "Photography", "0320-5566778", "8 years", "Rs. 700/hour", "Event and portrait photography"),
    ("Zohaib Zafar", "Tutoring", "0344-9988776", "6 years", "Rs. 400/hour", "Academic tutoring services"),
    ("Muhammaad Huzaifa", "Fitness Training", "0311-1122334", "10 years", "Rs. 500/hour", "Personal fitness training"),
    ("Taha Siddique", "Web Development", "0344-3344556", "9 years", "Rs. 600/hour", "Back end/Front end"),
    ("Saif Ali", "Event Planning", "0311-5566778", "8 years", "Rs. 800/hour", "Event planning and coordination"),
    ("Syed Saif Bin Waqqar", "Catering", "0320-9988776", "12 years", "Rs. 1000/hour", "Catering for events and parties"),
    ("Syed Mohtashim Ali", "Web Development", "0344-1122334", "5 years", "Rs. 250/hour", "Full stack development"),
    ("Faizan Ali Shah", "Web Development", "0311-3344556", "7 years", "Rs. 350/hour", "Web programmer"),
    ("Hassan Khan", "Interior Design", "0344-9988776", "10 years", "Rs. 900/hour", "Interior design and decorating"),
    ("Zain Shiekh", "Bike Mechanic", "0311-5566778", "5 years", "Rs. 400/hour", "Engine mechanic"),
    ("Zahid Khattak", "Web Development", "0320-1122334", "8 years", "Rs. 600/hour", "Database Administrator"),
    ("Kashif Khattak", "Web Development", "0344-3344556", "10 years", "Rs. 800/hour", "Website development and design"),
    ("Zaid Ansari", "Mobile App Development", "0311-9988776", "8 years", "Rs. 1000/hour", "Mobile app development"),
    ("Ibahat Hussain", "Legal Services", "0320-5566778", "15 years", "Rs. 1200/hour", "Legal consultation and representation"),
    ("Husnain Ali", "Financial Planning", "0311-1122334", "12 years", "Rs. 900/hour", "Financial planning services"),
    ("Sabir Shiekh", "Tax Preparation", "0344-3344556", "8 years", "Rs. 600/hour", "Tax preparation and filing"),
    ("Imran Shiekh", "Home Inspection", "0311-5566778", "10 years", "Rs. 700/hour", "Home inspection services"),
    ("Ijaz Ahmed", "Car Rental", "0320-9988776", "5 years", "Rs. 500/day", "Car rental services"),
    ("Aziz Ahmed", "Content Writing", "0344-1122334", "7 years", "Rs. 200/hour", "Copywriting"),
    ("Atif Khan", "Content Writing", "0311-3344556", "9 years", "Rs. 300/hour", "Business writing"),
    ("Naeem Ullah", "Security Services", "0320-5566778", "12 years", "Rs. 800/hour", "Security guard services"),
    ("Naveed sheikh", "Courier Services", "0311-9988776", "6 years", "Rs. 400/hour", "Courier and delivery services"),
    ("Mohsin Shah", "Language Translation", "0344-3344556", "8 years", "Rs. 500/hour", "Language translation services"),
    ("Yasir Ali", "Content Writing", "0311-5566778", "10 years", "Rs. 350/hour", "SEO writing"),
    ("Ahsan Ali", "Window Cleaning", "0320-9988776", "7 years", "Rs. 200/hour", "Window cleaning services"),
    ("Nadir Zaman", "Carpet Cleaning", "0344-1122334", "8 years", "Rs. 300/hour", "Carpet cleaning services"),
    ("Asif Khan", "Home Renovation", "0311-3344556", "15 years", "Rs. 1000/hour", "Home renovation and remodeling"),
    ("Qadir Zaman", "Welding", "0320-5566778", "10 years", "Rs. 700/hour", "Metal welding and fabrication"),
    ("Asif Khan", "Solar Panel Installation", "0311-9988776", "12 years", "Rs. 900/hour", "Solar panel installation"),
    ("Saif Shah", "Content Writing", "0344-3344556", "8 years", "Rs. 550/hour", "Blogging"),
    ("Tania Ahsan", "Dentistry", "0320-9988776", "20 years", "Rs. 1500/hour", "General dentistry services"),
    # Additional services (50 total)
    ("Umair Khan", "Graphic Design", "0311-3344556", "6 years", "Rs. 550/hour", "Logo and branding design"),
    ("Faisal Khan", "Photography", "0344-5566778", "7 years", "Rs. 750/hour", "Commercial and product photography"),
    ("Zubair Khan", "Tutoring", "0311-9988776", "5 years", "Rs. 300/hour", "Math and science tutoring"),
    ("Abdul Ahad", "Fitness Training", "0320-1122334", "9 years", "Rs. 650/hour", "Group fitness classes"),
    ("Yasin Magsi", "Graphic Design", "0344-3344556", "11 years", "Rs. 900/hour", "Packaging design"),
    ("Zainab Hussain", "Event Planning", "0311-5566778", "8 years", "Rs. 850/hour", "Wedding and party planning"),
    ("Adeel Ahmed", "Catering", "0320-9988776", "12 years", "Rs. 1100/hour", "Catering for special events"),
    ("Syed Noman Shah", "Graphic Design", "0344-1122334", "6 years", "Rs. 200/hour", "Publication design"),
    ("Syed Mohiuddin", "Graphic Design", "0311-3344556", "8 years", "Rs. 400/hour", "Branding design"),
    ("Abdullah Ahsan", "Interior Design", "0344-9988776", "10 years", "Rs. 800/hour", "Residential interior design"),
    ("Fenhas Robin", "Junk Removal", "0311-5566778", "7 years", "Rs. 450/hour", "Eco-friendly junk disposal"),
    ("Huzaifa Khan", "Pool Maintenance", "0320-1122334", "9 years", "Rs. 650/hour", "Pool equipment repair"),
    ("Zain Khan", "Web Development", "0344-3344556", "11 years", "Rs. 1000/hour", "E-commerce website development"),
    ("Zakir Ali", "Mobile App Development", "0311-9988776", "10 years", "Rs. 1200/hour", "iOS and Android app development"),
    ("Ali Raza", "Legal Services", "0320-5566778", "14 years", "Rs. 1500/hour", "Family law and divorce representation"),
    ("Arham Zahid", "Financial Planning", "0311-1122334", "13 years", "Rs. 1100/hour", "Retirement and investment planning"),
    ("Zakir Ali", "Tax Preparation", "0344-3344556", "8 years", "Rs. 700/hour", "Personal and business tax filing"),
    ("Bilal Hanif", "Home Inspection", "0311-5566778", "11 years", "Rs. 900/hour", "Pre-purchase and home safety inspections"),
    ("Abdul Majid", "Car Rental", "0320-9988776", "6 years", "Rs. 450/day", "Car rental services"),
    ("Numan Javed", "Bike Mechanic", "0344-1122334", "8 years", "Rs. 150/hour", "Wash and service technician"),
    ("Muhammad Nasir", "Elderly Care", "0311-3344556", "10 years", "Rs. 250/hour", "Companionship and assistance"),
    ("Ahmed Noor Khan", "Security Services", "0320-5566778", "12 years", "Rs. 850/hour", "Event and personal security"),
    ("Yasir Nawaz", "Courier Services", "0311-9988776", "7 years", "Rs. 300/hour", "Same-day delivery"),
    ("Aamir Saleem", "Language Translation", "0344-3344556", "9 years", "Rs. 400/hour", "Document translation services"),
    ("Naveed Jamal", "Gardening", "0311-5566778", "11 years", "Rs. 550/hour", "Lawn care and garden maintenance"),
    ("Raja Zohaib", "Window Cleaning", "0320-9988776", "8 years", "Rs. 200/hour", "Residential and commercial window cleaning"),
    ("Sarmad Danish", "Carpet Cleaning", "0344-1122334", "10 years", "Rs. 350/hour", "Carpet and upholstery cleaning"),
    ("Wakeel khan", "Home Renovation", "0311-3344556", "15 years", "Rs. 1200/hour", "Kitchen and bathroom remodeling"),
    ("Ateeq ul rehman", "Welding", "0320-5566778", "12 years", "Rs. 800/hour", "Custom metal fabrication"),
    ("Sheharyar	Faheem", "Solar Panel Installation", "0311-9988776", "14 years", "Rs. 1100/hour", "Residential solar panel installation"),
    ("Maqbool Ahmed", "Tree Trimming", "0344-3344556", "9 years", "Rs. 500/hour", "Tree pruning and removal"),
    ("Zainab Khan", "Dentistry", "0311-5566778", "18 years", "Rs. 1200/hour", "Cosmetic dentistry services"),
    ("Muhammad Ali", "Graphic Design", "0344-3344556", "7 years", "Rs. 500/hour", "Logo and graphic design"),
    ("Ateeq ul rehman", "Photography", "0320-9988776", "8 years", "Rs. 700/hour", "Portrait and event photography"),
    ("Rauf Shah", "Tutoring", "0344-1122334", "6 years", "Rs. 400/hour", "Math and English tutoring"),
    ("Zuhaib Masood", "Fitness Training", "0311-3344556", "9 years", "Rs. 550/hour", "Personal and group fitness training"),
    ("Luqman Sheikh", "Photography", "0344-9988776", "10 years", "Rs. 600/hour", "Portrait photography"),
    ("Abubakar Murtaza", "Event Planning", "0311-5566778", "8 years", "Rs. 800/hour", "Event coordination and management"),
    ("Kamal Abbasi", "Catering", "0320-1122334", "12 years", "Rs. 1000/hour", "Catering for weddings and events"),
    ("Noon Salam", "Photography", "0311-9988776", "5 years", "Rs. 250/hour", "Wedding photography"),
    ("Naqash touseef", "Pet Grooming", "0344-5566778", "7 years", "Rs. 350/hour", "Pet grooming and styling"),
    ("Saeed Sher", "Interior Design", "0320-3344556", "10 years", "Rs. 900/hour", "Residential and commercial design"),
    ("Zahoor Amjad", "Junk Removal", "0311-2233445", "7 years", "Rs. 400/hour", "Eco-friendly junk removal"),
    ("Awais faisal", "Pool Maintenance", "0322-3344556", "9 years", "Rs. 600/hour", "Pool cleaning and repair"),
    ("Shariq Uzair", "Web Development", "0311-9988776", "10 years", "Rs. 800/hour", "Website design and development"),
    ("Musayyab	Rehan", "Mobile App Development", "0344-1122334", "8 years", "Rs. 900/hour", "iOS and Android app development"),
    ("kalimullah Uzair", "Legal Services", "0311-3344556", "14 years", "Rs. 1200/hour", "Legal consultation and representation"),
    ("saeed Sher", "Financial Planning", "0320-9988776", "12 years", "Rs. 1000/hour", "Financial planning and investment advice"),
    ("Raza Mazhar", "Tax Preparation", "0311-5566778", "8 years", "Rs. 700/hour", "Tax filing and consulting"),
    ("Rashid Aslam", "Home Inspection", "0320-3344556", "10 years", "Rs. 800/hour", "Home inspection and assessment"),
    ("Sanaullah Khan", "Car Rental", "0311-2233445", "5 years", "Rs. 500/day", "Car rental services"),
    ("Wirda Ahsan", "Babysitting", "0322-3344556", "8 years", "Rs. 200/hour", "Childcare services"),
    ("Umair Ali", "Elderly Care", "0344-5566778", "10 years", "Rs. 300/hour", "Elderly companionship and assistance"),
    ("Ghulam Qadir", "Security Services", "0311-9988776", "12 years", "Rs. 800/hour", "Event and personal security"),
    ("Waqar Khan", "Courier Services", "0320-3344556", "7 years", "Rs. 400/hour", "Courier and delivery services"),
    ("Tawab Ali", "Language Translation", "0311-2233445", "8 years", "Rs. 500/hour", "Language translation and interpretation"),
    ("Yasin Owais", "Gardening", "0344-5566778", "10 years", "Rs. 350/hour", "Gardening and landscaping services"),
    ("Nizam Hafiz", "Window Cleaning", "0322-3344556", "7 years", "Rs. 200/hour", "Window cleaning for residential and commercial properties"),
    ("Ahmed Khan", "Carpet Cleaning", "0344-5566778", "8 years", "Rs. 300/hour", "Carpet and upholstery cleaning services"),
    ("Bisma Nawaz", "Home Renovation", "0311-9988776", "14 years", "Rs. 1000/hour", "Home renovation and remodeling"),
    ("Habib Bahadar", "Welding", "0320-3344556", "9 years", "Rs. 700/hour", "Metal welding and fabrication"),
    ("Abu Baqar Shiekh", "Solar Panel Installation", "0311-2233445", "11 years", "Rs. 900/hour", "Solar panel design and installation"),
    ("Ehtisham Anees", "Tree Trimming", "0344-5566778", "7 years", "Rs. 550/hour", "Tree trimming and pruning"),
            ("Faryal Shahid", "Dentistry", "0311-9988776", "18 years", "Rs. 1500/hour", "General dentistry services"),
        ]
        for name, service, contact, experience, prices, specialty in provider_data:
            self.helping_hand_project.add_service_provider(
                name, service, contact, experience, prices, specialty)

    def get_user_details(self):
        user_name = self.entry_name.get().strip()
        user_address = self.entry_address.get().strip()
        user_contact = self.entry_contact.get().strip()

        if not user_name or not user_address or not user_contact:
            messagebox.showerror("Error", "Please fill in all user details.")
            return

        # Additional validation for the contact number (numeric value)
        try:
            int(user_contact)
        except ValueError:
            messagebox.showerror(
                "Error", "Please enter a valid contact number.")
            return

        user = User(user_name, user_address, user_contact)
        self.show_providers(user)

    def show_providers(self, user):
        while True:
            user_input = simpledialog.askstring(
                "Service Needed", "Enter the type of service you are looking for (or type 'exit' to finish):")

            if user_input is None or user_input.strip() == "":
                messagebox.showinfo(
                    "No Service Entered", "Please enter a valid service.")
                continue

            if user_input.lower() == 'exit':
                break

            matching_providers = self.helping_hand_project.find_providers_by_service(
                user_input)

            if not matching_providers:
                messagebox.showinfo(
                    "No Providers", f"No matching service providers found for {user_input}.")
                continue

            provider_info = "\n".join(
                f"{provider.name} ({provider.specialty})" for provider in matching_providers
            )
            selected_provider_name = simpledialog.askstring(
                "Select Service Provider",
                f"Choose a service provider for {user_input} from the list:\n\n{provider_info}\n\nEnter the name (or type 'exit' to go back):"
            )

            if selected_provider_name is None or selected_provider_name.strip() == "":
                messagebox.showinfo(
                    "No Provider Selected", "Please select a valid service provider.")
                continue

            if selected_provider_name.lower() == 'exit':
                break

            selected_provider = next(
                (provider for provider in matching_providers if provider.name ==
                 selected_provider_name), None
            )

            if selected_provider is None:
                messagebox.showinfo(
                    "Invalid Provider", "No valid service provider selected."
                )
                continue

            # Check if the service is already selected
            existing_service = next(
                (service for service, provider in self.selected_services if service.lower() == user_input.lower()), None
            )

            if existing_service:
                # Ask if the user wants to change the provider for the existing service
                response = messagebox.askyesno(
                    "Service Already Selected", f"You have already selected a provider for {existing_service}. Do you want to change it?"
                )

                if response:
                    # Update the selected service
                    self.selected_services.remove((existing_service, selected_provider))
                else:
                    continue

            self.selected_services.append((user_input, selected_provider))

        self.review_and_confirm_services(user)

    def review_and_confirm_services(self, user):
        if not self.selected_services:
            messagebox.showinfo(
                "No Services Selected", "You haven't selected any services. Exiting."
            )
            return

        review_text = "Review Selected Services:\n\n"
        for service, provider in self.selected_services:
            review_text += f"Service: {service}\nProvider: {provider.name} ({provider.specialty}) - {provider.prices}\n\n"

        review_text += "Do you want to finalize these services?"

        response = messagebox.askyesno(
            "Review and Confirm", review_text)

        if response:
            self.finalize_services(user)
        else:
            # User wants to modify services
            self.modify_services(user)

    def modify_services(self, user):
        modify_text = "Modify Selected Services:\n\n"
        for service, provider in self.selected_services:
            modify_text += f"Service: {service}\nProvider: {provider.name} ({provider.specialty}) - {provider.prices}\n\n"

        modify_text += "Enter the service you want to modify (or type 'exit' to finish):"
        service_to_modify = simpledialog.askstring(
            "Modify Services", modify_text
        )

        if service_to_modify is None or service_to_modify.lower() == 'exit':
            self.review_and_confirm_services(user)
            return

        # Check if the service is in the selected services
        selected_service = next(
            (service for service, provider in self.selected_services if service.lower() == service_to_modify.lower()), None
        )

        if selected_service:
            # Find the provider for the selected service
            selected_provider = next(
                provider for service, provider in self.selected_services if service.lower() == selected_service.lower()
            )

            # Remove the selected service
            self.selected_services.remove((selected_service, selected_provider))

            # Show providers again for the modified service
            matching_providers = self.helping_hand_project.find_providers_by_service(
                selected_service)

            provider_info = "\n".join(
                f"{provider.name} ({provider.specialty}) - {provider.prices}" for provider in matching_providers
            )
            selected_provider_name = simpledialog.askstring(
                "Select Service Provider",
                f"Choose a service provider for {selected_service} from the list:\n\n{provider_info}\n\nEnter the name (or type 'exit' to go back):"
            )

            if selected_provider_name is None or selected_provider_name.strip() == "":
                messagebox.showinfo(
                    "No Provider Selected", "Please select a valid service provider.")
                self.modify_services(user)
                return

            if selected_provider_name.lower() == 'exit':
                self.modify_services(user)
                return

            selected_provider = next(
                (provider for provider in matching_providers if provider.name ==
                 selected_provider_name), None
            )

            if selected_provider is None:
                messagebox.showinfo(
                    "Invalid Provider", "No valid service provider selected."
                )
                self.modify_services(user)
                return

            # Add the modified service back to the selected services
            self.selected_services.append((selected_service, selected_provider))
        else:
            messagebox.showinfo(
                "Service Not Found", f"No matching service '{service_to_modify}' found in your selected services."
            )

        # Recursively call modify_services to allow further modifications
        self.modify_services(user)

    def finalize_services(self, user):
        # Finalize the selected services and display a confirmation message
        confirmation_text = "Finalized Services:\n\n"
        for service, provider in self.selected_services:
            confirmation_text += f"Service: {service}\nProvider: {provider.name}\nContact: {provider.contact}\nExperience: {provider.experience}\nSpecialty: {provider.specialty}\nPrice: {provider.prices}\n\n"

        messagebox.showinfo("Services Finalized", confirmation_text)

        # Optionally, you can perform additional actions here, such as storing the selected services in a database, etc.
        # Display a thank you message
        messagebox.showinfo("Thank You!", "Thank you for using Helping Hand Services!")
if __name__ == "__main__":
    root = tk.Tk()
    app = HelpingHandGUI(root)
    root.mainloop()
