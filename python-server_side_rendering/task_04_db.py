import os
import logging

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def generate_invitations(template, attendees):
    # Vérification du type des entrées
    if not isinstance(template, str):
        logging.error("Invalid input: template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        logging.error("Invalid input: attendees must be a list of dictionaries.")
        return

    # Vérification du contenu vide
    if not template.strip():
        logging.error("Template is empty, no output files generated.")
        return

    if not attendees:
        logging.info("No data provided, no output files generated.")
        return

    # Traitement de chaque invité
    for index, attendee in enumerate(attendees, start=1):
        output = template
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            output = output.replace(f"{{{key}}}", str(value))

        output_filename = f"output_{index}.txt"

        try:
            with open(output_filename, 'w') as f:
                f.write(output)
            logging.info(f"Generated {output_filename}")
        except Exception as e:
            logging.error(f"Failed to write file {output_filename}: {e}")
