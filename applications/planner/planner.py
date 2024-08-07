from flask import render_template, request, redirect, url_for
from datetime import datetime, timedelta
import json
import os

from . import planner

# Ścieżka do pliku z wydarzeniami
EVENTS_FILE = os.path.join(os.path.dirname(__file__), 'events.json')


def load_events():
    """Ładuje wydarzenia z pliku JSON."""
    if os.path.exists(EVENTS_FILE):
        with open(EVENTS_FILE, 'r') as file:
            return json.load(file)
    return []


def save_events(events):
    """Zapisuje wydarzenia do pliku JSON."""
    with open(EVENTS_FILE, 'w') as file:
        json.dump(events, file, indent=4)


@planner.route('/planner', methods=['GET', 'POST'])
def show_planner():
    """Wyświetla planer z wydarzeniami na nadchodzący tydzień."""
    events = load_events()

    if request.method == 'POST':
        event = {
            'title': request.form['title'],
            'date': request.form['date']
        }
        events.append(event)
        save_events(events)
        return redirect(url_for('planner.show_planner'))

    # Filtruj wydarzenia na nadchodzący tydzień
    today = datetime.now().date()
    week_later = today + timedelta(days=7)
    upcoming_events = [event for event in events if
                       today <= datetime.strptime(event['date'], '%Y-%m-%d').date() <= week_later]

    return render_template('planner.html', events=upcoming_events)


@planner.route('/planner/delete/<int:event_id>', methods=['POST'])
def delete_event(event_id):
    """Usuwa wydarzenie o podanym ID."""
    events = load_events()
    if 0 <= event_id < len(events):
        del events[event_id]
        save_events(events)
    return redirect(url_for('planner.show_planner'))
