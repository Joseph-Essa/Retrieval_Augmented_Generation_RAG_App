from .ragapp_base import SQLAlchemyBase
from sqlalchemy import Column, Integer, String, DateTime , func , ForeignKey,Boolean
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship
from sqlalchemy import Index
import uuid


class Asset(SQLAlchemyBase):
    
    __tablename__ = "assets"
    
    id = Column(Integer, primary_key=True,autoincrement=True)
    asset_uuid  = Column(UUID(as_uuid=True), default=uuid.uuid4 , unique=True , nullable=False)
    
    asset_type = Column(String,  nullable=False)
    asset_name = Column(String, nullable=False )
    asset_size = Column(Integer, nullable=False)
    asset_config = Column(JSONB, nullable=False ,default=dict)
    
    asset_project_id  = Column(Integer, ForeignKey("projects.id"), nullable=False)
    
    is_processed = Column(Boolean, nullable=False, default=False, server_default='false')
    
    project = relationship("Project", back_populates="assets")
    chunks = relationship("DataChunk", back_populates="asset")
    
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)
    
    __table_args__ = (
        Index('ix_asset_project_id',asset_project_id) , 
        Index('ix_asset_type',asset_type) ,
        Index('ix_asset_is_processed', is_processed),
    )