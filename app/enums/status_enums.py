from enum import Enum


class MeetingStatus(Enum):
    """Status possíveis para reuniões."""
    SCHEDULED = "SCHEDULED"
    CONFIRMED = "CONFIRMED"
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"
    NO_SHOW = "NO_SHOW"
    RESCHEDULED = "RESCHEDULED"


class FollowUpStatus(Enum):
    """Status possíveis para follow-ups."""
    PENDING = "pending"
    QUEUED = "queued"
    EXECUTED = "executed"
    FAILED = "failed"
    CANCELLED = "cancelled"
    SKIPPED = "skipped"


class FollowUpType(Enum):
    """Tipos de follow-up disponíveis."""
    MEETING_REMINDER = "meeting_reminder"
    DISQUALIFICATION = "disqualification"
    GENERAL = "general"
    REACTIVATION = "reactivation"


class LeadStatus(Enum):
    """Status possíveis para leads."""
    NEW = "new"
    CONTACTED = "contacted"
    QUALIFIED = "qualified"
    MEETING_SCHEDULED = "meeting_scheduled"
    PROPOSAL_SENT = "proposal_sent"
    CLOSED_WON = "closed_won"
    CLOSED_LOST = "closed_lost"
    DISQUALIFIED = "disqualified"


class ConversationStatus(Enum):
    """Status possíveis para conversas."""
    ACTIVE = "active"
    INACTIVE = "inactive"
    ENDED = "ended"
    TRANSFERRED = "transferred"


class MessageType(Enum):
    """Tipos de mensagem."""
    TEXT = "text"
    AUDIO = "audio"
    IMAGE = "image"
    DOCUMENT = "document"
    VIDEO = "video"
    LOCATION = "location"
    CONTACT = "contact"