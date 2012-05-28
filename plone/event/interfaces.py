from zope.interface import Interface, Attribute


class IEvent(Interface):
    """ Event type marker interface.

    """


class IEventRecurrence(Interface):
    """ Event type marker interface for events with an RFC5545 compatible
        recurrence definition.

    """


class ICalendarAccessor(Interface):
    """ Generic calendar accessor adapter interface.

        A calendar is a collection of calendar components, like events.

    """
    uid = Attribute(u"UID of the calendar. Autogenerated, read only.")
    # rw attributes
    title = Attribute(u"Calendar title.")
    description = Attribute(u"Calendar description text.")
    timezone = Attribute(u"Default timezone of the calendar.")

    def items(self):
        """ Return a list of calendar component items, like events.

        """


class IEventAccessor(Interface):
    """ Event type generic accessor adapter interface.

        A specific adapter implementation should be provided by the individual
        content type packages.

    """

    # ro attributes
    uid = Attribute(u"UID of the event. Autogenerated, read only.")
    created = Attribute(u"Python datetime of the event creation timestamp.")
    last_modified = Attribute(u"""Python datetime of the last modified
                                  timestamp.""")
    duration = Attribute(u"Duration of the event. Computed attribute.")

    # reference
    url = Attribute(u"""Cannonical, unique url of the event. External events
                        are referenced by the origin url unless explicitly
                        set.""")

    # rw attributes
    title = Attribute(u"Event title.")
    description = Attribute(u"Event description text.")
    start = Attribute(u"Event start date as Python datetime.")
    end = Attribute(u"Event end date as Python datetime.")
    whole_day = Attribute(u"Event lasts whole day.")
    timezone = Attribute(u"Timezone of the event. A pytz timezone identifier.")
    recurrence = Attribute(u"RFC5545 compatible recurrence definition.")
    location = Attribute(u"Location of the event.")
    attendees = Attribute(u"List of attendees.")
    contact_name = Attribute(u"Contact name.")
    contact_email = Attribute(u"Contact email.")
    contact_phone = Attribute(u"Contact phone.")
    event_url = Attribute(u"Website of the event.")
    subjects = Attribute(u"Categories.")
    text = Attribute(u"Body text of the event.")


class IRecurrenceSupport(Interface):
    """ Event type recurrence adatper.

    """

    def occurrences(self, range_start, range_end):
        """ Return a list of IOccurrence objects with custom attributes of the
            specific occurrence set.

            @param range_start: Search for occurrences after this date.
                                Python datetime.

            @param range_end: Search for occurrences before this date.
                              Python datetime.
        """
        pass


class IVEvent(Interface):
    """ RFC5545 Event schema

    ; The following are REQUIRED,
    ; but MUST NOT occur more than once.
    ;
    dtstamp / uid /
    ;
    ; The following is REQUIRED if the component
    ; appears in an iCalendar object that doesn't
    ; specify the "METHOD" property; otherwise, it
    ; is OPTIONAL; in any case, it MUST NOT occur
    ; more than once.
    ;
    dtstart /
    ;
    ; The following are OPTIONAL,
    ; but MUST NOT occur more than once.
    ;
    class / created / description / geo /
    last-mod / location / organizer / priority /
    seq / status / summary / transp /
    url / recurid /
    ;
    ; The following is OPTIONAL,
    ; but SHOULD NOT occur more than once.
    ;
    rrule /
    ;
    ; Either 'dtend' or 'duration' MAY appear in
    ; a 'eventprop', but 'dtend' and 'duration'
    ; MUST NOT occur in the same 'eventprop'.
    ;
    dtend / duration /
    ;
    ; The following are OPTIONAL,
    ; and MAY occur more than once.
    ;
    attach / attendee / categories / comment /
    contact / exdate / rstatus / related /
    resources / rdate / x-prop / iana-prop

    """
    dtstart = Attribute(u"Start Date/Time")
    dtend = Attribute(u"End Date/Time")
    duration = Attribute(u"Duration")
    rrule = Attribute(u"Recurrence Rule")
    description = Attribute(u"Description")
    location = Attribute(u"Location")
    summary = Attribute(u"Summary")
    url = Attribute(u"Url")
    attendee = Attribute(u"Attendee")
    categories = Attribute(u"Categories")
    contact = Attribute(u"Contact")

    exdate = Attribute(u"Exdate")
    rdate = Attribute(u"Rdate")

    dtstamp = Attribute(u"Timestamp")
    uid = Attribute(u"Unique identifier")
    klass = Attribute(u"Class") # class
    created = Attribute(u"Created")
    geo = Attribute(u"Geo")
    last_mod = Attribute(u"Last Modified") # last-mod
    organizer = Attribute(u"Organizer")
    priority = Attribute(u"Priority")
    seq = Attribute(u"Seq")
    status = Attribute(u"Status")
    transp = Attribute(u"Transp")
    recurid = Attribute(u"Recurid")
    attach = Attribute(u"Attach")
    comment = Attribute(u"Comment")
    rstatus = Attribute(u"Rstatus")
    related = Attribute(u"Related")
    resources = Attribute(u"Resources")
    x_prop = Attribute(u"X Prop") # x-prop
    iana_prop = Attribute(u"Iana Prop") # iana-prop


    start = Attribute(u"Event start date")
    end = Attribute(u"Event end date")
    timezone = Attribute(u"Timezone of the event")
    recurrence = Attribute(u"RFC5545 compatible recurrence definition")
    whole_day = Attribute(u"Event lasts whole day")
    location = Attribute(u"Location of the event")
    text = Attribute(u"Summary of the event")
    attendees = Attribute(u"List of attendees")
    event_url = Attribute(u"Website of the event")
    contact_name = Attribute(u"Contact name")
    contact_email = Attribute(u"Contact email")
    contact_phone = Attribute(u"Contact phone")
